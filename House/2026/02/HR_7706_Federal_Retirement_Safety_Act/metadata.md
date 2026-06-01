# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7706?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7706
- Title: Federal Retirement Safety Act
- Congress: 119
- Bill type: HR
- Bill number: 7706
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-10T08:05:48Z
- Update date including text: 2026-04-10T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7706",
    "number": "7706",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Federal Retirement Safety Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:48Z",
    "updateDateIncludingText": "2026-04-10T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-02-25T14:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "OK"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "WI"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "AZ"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7706ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7706\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Neguse (for himself, Mrs. Bice , Ms. Moore of Wisconsin , Mrs. Dingell , Ms. Norton , Ms. Tlaib , and Ms. Lee of Pennsylvania ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo change the spousal notification and consent requirements for the payment of lump-sum retirement benefits in cases of domestic violence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Retirement Safety Act .\n#### 2. Lump-sum retirement benefit notice and consent requirements in case of domestic violence\n##### (a) Federal employee retirement system\nSection 8424(b) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by adding at the end the following new subparagraph:\n(C) Under the regulations, the Office shall provide that paragraph (1)(A) may be waived with respect to a spouse or former spouse to the extent necessary to protect the safety of the employee or Member, or any other person, if the employee or Member establishes to the satisfaction of the Office that\u2014 (i) such spouse or former spouse engaged in conduct constituting a domestic violence crime (as defined in section 3561(b) of title 18) against the employee or Member; and (ii) providing notice in accordance with such paragraph poses a risk to the safety of the employee or Member or any other person. ; and\n**(2)**\nby adding at the end the following new paragraphs:\n(4) (A) The Office shall prescribe regulations that provide\u2014 (i) that, notwithstanding paragraph (1)(B), the lump-sum credit may be paid without the consent of a spouse or former spouse to the extent permitted by the applicable court order and necessary to protect the safety of the employee or Member, or any other person, if the employee or Member establishes to the satisfaction of the Office the criteria described in subparagraph (B); and (ii) procedures to obtain the consent of a spouse or former spouse for the payment of the lump-sum credit in a manner that protects the safety of the employee or Member if the lump-sum credit may not be paid in accordance with the applicable court order without obtaining such consent and the employee or Member establishes to the satisfaction of the Office the criteria described in subparagraph (B). (B) The criteria described in this subparagraph are\u2014 (i) that the spouse or former spouse engaged in conduct constituting a domestic violence crime (as defined in section 3561(b) of title 18) against the employee or Member; and (ii) obtaining consent in accordance with the regulations under paragraph (1)(B) poses a risk to the safety of the employee or Member or any other person. (5) For the purposes of paragraphs (2)(C) and (4)(A), an employee or Member establishes to the satisfaction of the Office the criteria described in paragraph (4)(B) with respect to a spouse or former spouse for payment of the lump-sum credit if such employee or Member self-certifies to the Office in writing that such spouse or former spouse engaged in conduct constituting a domestic violence crime (as defined in section 3561(b) of title 18) against the employee or Member during the one-year period ending on the date on which such employee or Member submits to the Office the application for such payment. .\n##### (b) Civil service retirement system\nSection 8342(j) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by adding at the end the following new subparagraph:\n(C) Under the regulations, the Office shall provide that paragraph (1)(A) may be waived with respect to a spouse or former spouse to the extent necessary to protect the safety of the employee or Member, or any other person, if the employee or Member establishes to the satisfaction of the Office that\u2014 (i) such spouse or former spouse engaged in conduct constituting a domestic violence crime (as defined in section 3561(b) of title 18) against the employee or Member; and (ii) providing notice in accordance with such paragraph poses a risk to the safety of the employee or Member or any other person. ; and\n**(2)**\nby adding at the end the following new paragraphs:\n(4) (A) The Office shall prescribe regulations that provide\u2014 (i) that, notwithstanding paragraph (1)(B), the lump-sum credit may be paid without the consent of a spouse or former spouse to the extent permitted by the applicable court order and necessary to protect the safety of the employee or Member, or any other person, if the employee or Member establishes to the satisfaction of the Office the criteria described in subparagraph (B); and (ii) procedures to obtain the consent of a spouse or former spouse for the payment of the lump-sum credit in a manner that protects the safety of the employee or Member if the lump-sum credit may not be paid in accordance with the applicable court order without obtaining such consent and the employee or Member establishes to the satisfaction of the Office the criteria described in subparagraph (B). (B) The criteria described in this subparagraph are\u2014 (i) that the spouse or former spouse engaged in conduct constituting a domestic violence crime (as defined in section 3561(b) of title 18) against the employee or Member; and (ii) obtaining consent in accordance with the regulations under paragraph (1)(B) poses a risk to the safety of the employee or Member or any other person. (5) For the purposes of paragraphs (2)(C) and (4)(A), an employee or Member establishes to the satisfaction of the Office the criteria described in paragraph (4)(B) with respect to a spouse or former spouse for payment of the lump-sum credit if such employee or Member self-certifies to the Office in writing that such spouse or former spouse engaged in conduct constituting a domestic violence crime (as defined in section 3561(b) of title 18) against the employee or Member during the one-year period ending on the date on which such employee or Member submits to the Office the application for such payment. .\n##### (c) Applicability\n**(1) In general**\nThe amendments made by this Act shall not affect the requirements to provide notice to or obtain consent from an individual under section 8342(j) or 8424(b) of title 5, United States Code, with respect to a lump-sum credit (as such term is defined under section 8331 or 8401 of such title) to the extent that such notice or consent would have been required if the payment of such lump-sum credit occurred prior to the date of the enactment of this Act, except that, to the extent that such amendments would, but for this subsection, affect such a requirement with respect to an individual, the Director of the Office of Personnel Management shall establish procedures to provide such notice to or obtain consent from such individual in a manner that ensures the safety of the relevant employee or Member.\n**(2) Employee; lump-sum; member defined**\nIn this subsection, the terms employee , lump-sum , and Member \u2014\n**(A)**\nwith respect to section 8342(j) of title 5, United States Code, have the meanings given such terms, respectively, in section 8331 of such title; and\n**(B)**\nwith respect to section 8424(b) of such title, have the meanings given such terms, respectively, in section 8401 of such title.\n##### (d) Regulations\nNot later than one year after the date of the enactment of this Act, the Director of the Office of Personnel Management shall issue regulations implementing the amendments made by this Act.\n##### (e) Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is one year after the date of the enactment of this Act.",
      "versionDate": "2026-02-25",
      "versionType": "Introduced in House"
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-04T15:58:41Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7706ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Federal Retirement Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T09:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Retirement Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-03T09:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To change the spousal notification and consent requirements for the payment of lump-sum retirement benefits in cases of domestic violence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-03T09:48:30Z"
    }
  ]
}
```
