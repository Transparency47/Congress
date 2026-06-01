# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/926?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/926
- Title: Saving Our Veterans Lives Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 926
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-02-11T12:03:24Z
- Update date including text: 2026-02-11T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/926",
    "number": "926",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Saving Our Veterans Lives Act of 2025",
    "type": "S",
    "updateDate": "2026-02-11T12:03:24Z",
    "updateDateIncludingText": "2026-02-11T12:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-12-10T21:00:04Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-10T21:00:04Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-11T15:45:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "MT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "ME"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "AZ"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "AR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s926is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 926\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. King (for himself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to establish a program to furnish to certain veterans items used for the secure storage of firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Saving Our Veterans Lives Act of 2025 .\n#### 2. Program of Department of Veterans Affairs to furnish to certain veterans items used for secure storage of firearms\n##### (a) Program\n**(1) In general**\nSubchapter II of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section:\n1720M. Program to furnish to eligible individuals items intended to be used for the secure storage of firearms (a) In general The Secretary shall carry out a program to provide to an eligible individual, upon the request of the eligible individual\u2014 (1) a covered item or a redeemable voucher to aid in the distribution of a covered item; and (2) information relating to the benefits of, and options for, secure firearm storage. (b) Distribution of covered items In carrying out the program under subsection (a), the Secretary is authorized to work with organizations that have experience, expertise, and business knowledge regarding secure firearm storage and secure firearm storage devices. (c) Public education campaign (1) In general The Secretary shall design and carry out a public education campaign to inform eligible individuals of the availability of covered items under the program under subsection (a). (2) Partnership In carrying out the public education campaign required under paragraph (1), the Secretary may partner with organizations that have experience with respect to secure firearm storage devices. (3) Assurance about lawful ownership of firearms The Secretary shall include in the public education campaign required under paragraph (1) material that assures eligible individuals that their participation in the program under subsection (a) does not impact lawful ownership of firearms. (d) Reports to Congress Not later than October 1, 2025, and not less frequently than annually thereafter, the Secretary shall submit to the appropriate committees of Congress a report that includes\u2014 (1) a description of the program under subsection (a) in a manner consistent with applicable law; (2) during the period covered by the report, the number of covered items distributed by the Veterans Health Administration and the number of covered items redeemed outside of the Veterans Health Administration under the program; (3) an assessment of efforts made to increase outreach and distribution of covered items under the program to eligible individuals who are not enrolled in the system of annual patient enrollment of the Department established and operated under section 1705 of this title; (4) an assessment of any obstacles to increasing outreach to eligible individuals who are enrolled in such system and those who are not enrolled in such system; and (5) an identification of additional steps that will be taken during the one-year period after the submission of the report to improve the processes through which eligible individuals receive a covered item under the program. (e) Definitions In this section: (1) The term appropriate committees of Congress means\u2014 (A) the Committee on Veterans' Affairs and the Committee on Appropriations of the Senate; and (B) the Committee on Veterans' Affairs and the Committee on Appropriations of the House of Representatives. (2) The term covered item means a lockbox that\u2014 (A) is used for the secure storage of a firearm and ammunition; (B) is designed, intended, and marketed to prevent unauthorized access to a firearm or ammunition; (C) may be unlocked only by means of a key, combination, or other similar means; (D) is in compliance with the standard of the American Society for Testing and Materials F2456\u201320, or any successor standard; (E) is manufactured in the United States; and (F) is not eligible or intended for commercial or individual resale. (3) The term eligible individual means\u2014 (A) a veteran; or (B) an individual described in section 1720I(b) of this title. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1720L the following new item:\n1720M. Program to furnish to eligible individuals items intended to be used for the secure storage of firearms. .\n##### (b) Education and training\nThe Secretary of Veterans Affairs shall\u2014\n**(1)**\nin consultation with representatives of organizations and agencies that are subject to a memorandum of understanding with the Secretary on preventing veteran suicide and other such entities as the Secretary determines appropriate\u2014\n**(A)**\ndevelop an informational video on secure storage of firearms as a suicide prevention strategy; and\n**(B)**\npublish such informational video on an internet website of the Department of Veterans Affairs; and\n**(2)**\npublish information to inform individuals who participate in the program under section 1720M of title 38, United States Code (as added by subsection (a)(1)) that any lockbox furnished pursuant to such program is not eligible or intended for commercial or individual resale.\n##### (c) Rule of construction\nNothing in this Act or the amendments made by this Act may be construed\u2014\n**(1)**\nto collect personally identifiable information of an individual who participates in the program under section 1720M of title 38, United States Code (as added by subsection (a)(1)) for the purposes of tracking firearm ownership;\n**(2)**\nto require any such individual to register a firearm with the Department of Veterans Affairs, or any other Federal, State, Tribal, or local unit of government;\n**(3)**\nto require mandatory firearm storage for any such individual;\n**(4)**\nto prohibit any such individual from purchasing, owning, or possessing a firearm under section 922 of title 18, United States Code;\n**(5)**\nto discourage the lawful ownership of firearms; or\n**(6)**\nto create or maintain a list of individuals participating in such program.\n##### (d) Authorization of appropriations\nThere are authorized to be appropriated to the Secretary of Veterans Affairs $5,000,000 for each of fiscal years 2026 through 2036 to carry out this section and the amendments made by this section.",
      "versionDate": "2025-03-11",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-12",
        "text": "Referred to the Subcommittee on Oversight and Investigations."
      },
      "number": "1987",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Saving Our Veterans Lives Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-12T21:02:46Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-12-12T21:02:39Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-12-12T21:02:51Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-12-12T21:02:58Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-12-12T21:03:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-09T15:32:24Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s926is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Saving Our Veterans Lives Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Saving Our Veterans Lives Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to direct the Secretary of Veterans Affairs to establish a program to furnish to certain veterans items used for the secure storage of firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:18:29Z"
    }
  ]
}
```
