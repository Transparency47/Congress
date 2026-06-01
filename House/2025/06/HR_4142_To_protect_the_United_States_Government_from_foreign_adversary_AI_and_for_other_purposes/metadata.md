# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4142?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4142
- Title: No Adversarial AI Act
- Congress: 119
- Bill type: HR
- Bill number: 4142
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2025-12-05T22:55:25Z
- Update date including text: 2025-12-05T22:55:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4142",
    "number": "4142",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "No Adversarial AI Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:55:25Z",
    "updateDateIncludingText": "2025-12-05T22:55:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:02:15Z",
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
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "IL"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "IL"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4142ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4142\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Moolenaar (for himself, Mr. Krishnamoorthi , Mr. LaHood , and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo protect the United States Government from foreign adversary AI and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Adversarial AI Act .\n#### 2. Determination of foreign adversary AI\n##### (a) Development of list\nNot later than 60 days after the date of the enactment of this Act, the Federal Acquisition Security Council shall develop a list containing any artificial intelligence that is produced or developed by a foreign adversary.\n##### (b) Publication of list\nNot later than 180 days after the date of the enactment of this Act, the Director of the Office of Management and Budget, in coordination with the Federal Acquisition Security Council, shall publish on a publicly available website the list developed pursuant to subsection (a).\n##### (c) Updates to list\n**(1) In general**\nThe Federal Acquisition Security Council shall update the list developed pursuant to subsection (a) not less than every 180 days.\n**(2) Removal from list**\nThe Federal Acquisition Security Council may remove artificial intelligence from the list pursuant to subsection (a) if\u2014\n**(A)**\nthe person that owns such artificial intelligence submits to the Federal Acquisition Security Council a certification that the product or service is not produced or developed by a foreign adversary, including information in support of such certification; and\n**(B)**\nthe Federal Acquisition Security Council\u2014\n**(i)**\nreviews such certification and information; and\n**(ii)**\ncertifies that the artificial intelligence is not produced or developed by a foreign adversary.\n#### 3. Prohibition on acquiring and use of foreign adversary AI\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the head of an executive agency, in coordination with the Federal Acquisition Security Council, shall review and consider for exclusion and removal of artificial intelligence provided by a covered foreign adversary entity included on the list developed pursuant to section 2(a), barring an approved exception through the process described in subsection (c).\n##### (b) Authorities relating to mitigating risks in the acquisition and use of foreign adversary AI\nThe head of an executive agency shall, at a minimum, use the authorities in section 4713 of title 41, United States Code, to consider for exclusion and removal artificial intelligence provided by a covered foreign adversary entity included on the list developed pursuant to section 2(a).\n##### (c) Exceptions and notice\nUpon written notice to the Director of the Office of Management and Budget and the appropriate committees of Congress, the head of an executive agency may approve an exception to the determinations under subsection (a) if the head of the agency determines that acquiring, obtaining, or using the artificial intelligence is necessary\u2014\n**(1)**\nfor the purpose of scientifically valid research (as defined in section 102 of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9501 ));\n**(2)**\nfor the purpose of evaluation, training, testing, or analysis;\n**(3)**\nfor the purpose of conducting counterterrorism or counterintelligence activities; or\n**(4)**\nto avoid jeopardizing the performance of mission critical functions.\n##### (d) Definitions\nIn this section:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives.\n**(2) Artificial intelligence**\nThe term artificial intelligence has the meaning given the term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 940 ) and includes the artificial intelligence systems and techniques described in paragraphs (1) through (5) of section 238(g) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. 4061 note prec.).\n**(3) Executive agency**\nThe term executive agency has the meaning given the term Executive agency in section 105 of title 5, United States Code.\n**(4) Foreign adversary**\nThe term foreign adversary has the meaning given the term covered nation in section 4872(f)(2) of title 10, United States Code.\n**(5) Foreign adversary entity**\nThe term foreign adversary entity means\u2014\n**(A)**\na foreign adversary;\n**(B)**\na foreign person that is domiciled in, is headquartered in, has its principal place of business in, or is organized under the laws of a foreign adversary country;\n**(C)**\nan entity with respect to which a foreign person or combination of foreign persons described in subparagraph (A) or (B) directly or indirectly owns at least a 20 percent stake; or\n**(D)**\na person subject to the direction or control of a foreign person or entity described in subparagraph (A), (B), or (C).",
      "versionDate": "2025-06-25",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-06-25",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2177",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Adversarial AI Act",
      "type": "S"
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
        "updateDate": "2025-07-31T22:38:52Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4142ih.xml"
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
      "title": "No Adversarial AI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Adversarial AI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect the United States Government from foreign adversary AI and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T02:48:21Z"
    }
  ]
}
```
