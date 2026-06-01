# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5028?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5028
- Title: SAFE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5028
- Origin chamber: House
- Introduced date: 2025-08-22
- Update date: 2025-09-12T20:51:37Z
- Update date including text: 2025-09-12T20:51:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-22: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-08-22: Introduced in House

## Actions

- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-22",
    "latestAction": {
      "actionDate": "2025-08-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5028",
    "number": "5028",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SAFE Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-12T20:51:37Z",
    "updateDateIncludingText": "2025-09-12T20:51:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-22",
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
      "actionDate": "2025-08-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-22",
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
          "date": "2025-08-22T13:00:45Z",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5028ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5028\nIN THE HOUSE OF REPRESENTATIVES\nAugust 22, 2025 Mr. Min (for himself and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend section 552a of title 5, United States Code, to provide for the liability of Federal personnel for intentional or willful violations of such section, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Security and Accountability For Everyone Act of 2025 or the SAFE Act of 2025 .\n#### 2. Liability of the United States and Federal personnel under the Privacy Act\nSection 552a of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (12), by striking and at the end;\n**(B)**\nin paragraph (13), by inserting striking the period at the end and inserting the following: , and covered special Government employees; and ; and\n**(C)**\nby adding at the end the following:\n(14) the term covered special Government employee means a special Government employee (as such term is defined in section 202 of title 18) who\u2014 (A) does not serve on an advisory committee (as such term is defined in section 1001); (B) serves in a position listed in level GS\u201313 or higher of the General Schedule, an equivalent position in the Senior Executive Service, a senior level position, a scientific or professional position, or an equivalent position in an agency-specific pay scale; and (C) does not serve in a position that is designated for an intern or unpaid student volunteer serving pursuant to section 3111, or similar statutory authority. .\n**(2)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (C), by striking , and consequently a determination is made which is adverse to the individual ; and\n**(ii)**\nin subparagraph (D), by striking , in such a way as to have an adverse effect on an individual ; and\n**(B)**\nby adding at the end the following:\n(6) Intentional or willful violations by Federal personnel (A) In general Whenever Federal personnel engages in conduct described in subparagraph (C) or (D) of paragraph (1) that is intentional or willful and that results in demonstrable harm to an individual, the individual may bring a civil action against the Federal personnel, and the district courts of the United States shall have jurisdiction in the matters under the provisions of this subsection. (B) No immunity It shall not be a defense to an action under this paragraph alleging intentional or willful conduct that the Federal personnel is immune from liability. (C) Remedies In an action brought under this paragraph, the Federal personnel shall be personally liable to the individual in an amount equal to the amount authorized under paragraph (4). The United States shall not be liable for such amount. (D) Reimbursement of Department of Justice If an attorney for the Department of Justice represents Federal personnel in an action under this paragraph, and the Federal personnel is found to have engaged in conduct described in subparagraph (C) or (D) of paragraph (1) that was intentional or willful, the court shall enter an order requiring the Federal personnel to pay to the Department of Justice an amount that is equal to the cost of such representation. (7) Parens patriae In any case in which the attorney general of a State has reason to believe that an interest of the residents of that State has been or is threatened or adversely affected by conduct described in subparagraph (C) or (D) of paragraph (1) that is intentional or willful, the attorney general of the State, as parens patriae, may bring a civil action against the agency or the Federal personnel, as applicable, on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief. .",
      "versionDate": "2025-08-22",
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
        "updateDate": "2025-09-12T20:51:37Z"
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
      "date": "2025-08-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5028ih.xml"
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
      "title": "SAFE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-23T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-23T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Security and Accountability For Everyone Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-23T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 552a of title 5, United States Code, to provide for the liability of Federal personnel for intentional or willful violations of such section, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-23T08:18:21Z"
    }
  ]
}
```
