# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1164?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1164
- Title: Directing Members required to reimburse the Treasury for payments related to certain claims to appear before the Clerk for public disclosure of the reasons for the reimbursement.
- Congress: 119
- Bill type: HRES
- Bill number: 1164
- Origin chamber: House
- Introduced date: 2026-04-13
- Update date: 2026-05-14T08:08:43Z
- Update date including text: 2026-05-14T08:08:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-13: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-13 - IntroReferral: Submitted in House
- Latest action: 2026-04-13: Submitted in House

## Actions

- 2026-04-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-13 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-13",
    "latestAction": {
      "actionDate": "2026-04-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1164",
    "number": "1164",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Directing Members required to reimburse the Treasury for payments related to certain claims to appear before the Clerk for public disclosure of the reasons for the reimbursement.",
    "type": "HRES",
    "updateDate": "2026-05-14T08:08:43Z",
    "updateDateIncludingText": "2026-05-14T08:08:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-04-13T18:30:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-13T18:30:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "OK"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "AL"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "GA"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "AZ"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "IN"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "AR"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "KS"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NC"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "AL"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "IA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1164ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1164\nIN THE HOUSE OF REPRESENTATIVES\nApril 13, 2026 Mrs. Bice (for herself, Mr. Brecheen , Mr. Moore of Alabama , and Mr. Carter of Georgia ) submitted the following resolution; which was referred to the Committee on House Administration , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nDirecting Members required to reimburse the Treasury for payments related to certain claims to appear before the Clerk for public disclosure of the reasons for the reimbursement.\n#### 1. Obligations of Members who must reimburse the United States Treasury for certain payments\n##### (a) OCWR report to Committee on House Administration\nAfter the Executive Director of the Office of Congressional Workplace Rights submits a report under section 1102 of the Legislative Branch Appropriations Act, 2014 ( 2 U.S.C. 1387 ), to the Committee on House Administration, the Committee shall immediately transmit the report to the Clerk, and the Committee, in coordination with the Clerk, shall distribute\u2014\n**(1)**\na copy of the report to\u2014\n**(A)**\neach Member who must reimburse the United States Treasury for a payment related to a claim under section 415(d) of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1415(d) ); and\n**(B)**\neach former Member who must reimburse the United States Treasury for a payment related to a claim under section 415(d) of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1415(d) ); and\n**(2)**\na copy of the report and a list of the Members and former Members described in paragraph (1) to the Sergeant-at-Arms.\n##### (b) Public reading\n**(1) In general**\nSubject to this subsection, each Member who receives the report described in subsection (a) shall personally appear in the well of the House of Representatives, at a time determined by the Clerk while the House is in session, and the Clerk shall conduct a public reading of the name of the Member, the amount of any payment referred to in the report subject to reimbursement by the Member, whether the Member has completed reimbursement of such a payment, and the information included in the report related to the payment.\n**(2) Determination of time**\nA public reading under paragraph (1) related to a Member with respect to any part of a report described in subsection (a) shall be conducted\u2014\n**(A)**\nnot earlier than 14 days after the date on which the Clerk receives a copy of the report under subsection (a); and\n**(B)**\non the earliest date available after the Clerk receives notice from the Member that the Member is available for the public reading.\n##### (c) Enforcement\n**(1) In general**\nA Member who receives the report described in subsection (a) and who does not comply with subsection (b) within 30 days after the date on which the Member receives the report shall cease, until the Member complies with subsection (b), any activity in connection with\u2014\n**(A)**\na committee to which the Member is appointed; and\n**(B)**\nany duty, responsibility, or obligation of the Member, as determined by the Speaker or the Minority Leader, as the case may be, related to the Member being\u2014\n**(i)**\nthe Speaker;\n**(ii)**\nthe Majority Leader;\n**(iii)**\nthe Minority Leader; or\n**(iv)**\nin a party caucus or conference leadership position (as such term is used in clause 10(b) of rule XXIII of the Rules of the House of Representatives).\n**(2) Notice to committees and leadership**\nOn the date that is 30 days after the designated staff employee of the Committee on House Administration carries out subsection (a) with respect to a report described in the subsection, for each Member named in the report who does not comply with subsection (b) by such date, the Clerk shall provide notice to the Speaker, the Minority Leader, and the chair and ranking minority member of each committee to which the Member is appointed that the Member is not in compliance with subsection (b).\n**(3) Committee on Ethics**\nAn allegation of failure to comply with this resolution or of material deception in complying with this resolution shall be treated as a separate matter for investigation or action by the Committee on Ethics from any act, allegation, or claim related to, or referred to in, any report described in subsection (a).\n##### (d) Former Members\n**(1) In general**\nA former Member who receives the report described in subsection (a) may not be admitted to the Hall of the House or rooms leading thereto, under rule IV of the Rules of the House of Representatives, until the former Member completes reimbursement of the amounts paid by the United States Treasury referred to in the report.\n**(2) Public reading**\nA former Member who completes reimbursement in accordance with paragraph (1) shall have the privilege of admission to the Hall of the House or rooms leading thereto restored to the former Member, to the extent provided under rule IV of the Rules of the House of Representatives, if the former Member carries out the provisions applicable to a Member under subsection (b) as if the former Member is a Member, and the former Member shall be admitted to the Hall of the House if such admission is necessary to carry out the subsection.\n**(3) Assistance of the Clerk**\nThe Clerk shall carry out the provisions applicable to the Clerk under subsection (b) with respect to a former Member who, in carrying out paragraph (2), carries out the provisions applicable to a Member under subsection (b) as if the former Member is a Member.\n**(4) Notice to Sergeant-at-Arms**\nThe Clerk shall notify the Sergeant-at-Arms of any former Member who, having lost the privilege of admission to the Hall of the House or rooms leading thereto under paragraph (1), has such privilege restored after carrying out paragraph (2).\n##### (e) Member defined\nIn this resolution, the term Member means a Member, a Delegate, or a Resident Commissioner of the House of Representatives.",
      "versionDate": "2026-04-13",
      "versionType": "IH"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Congress",
        "updateDate": "2026-04-17T19:05:27Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1164ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Directing Members required to reimburse the Treasury for payments related to certain claims to appear before the Clerk for public disclosure of the reasons for the reimbursement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T08:18:46Z"
    },
    {
      "title": "Directing Members required to reimburse the Treasury for payments related to certain claims to appear before the Clerk for public disclosure of the reasons for the reimbursement.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T08:05:39Z"
    }
  ]
}
```
