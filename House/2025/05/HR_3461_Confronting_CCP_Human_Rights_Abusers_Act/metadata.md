# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3461?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3461
- Title: Confronting CCP Human Rights Abusers Act
- Congress: 119
- Bill type: HR
- Bill number: 3461
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-15T08:07:27Z
- Update date including text: 2026-05-15T08:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3461",
    "number": "3461",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Confronting CCP Human Rights Abusers Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:27Z",
    "updateDateIncludingText": "2026-05-15T08:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AL"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3461ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3461\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Ogles (for himself, Mr. Moolenaar , Ms. Stefanik , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the inclusion of the Ministry of Public Security\u2019s Institute of Forensic Science of China on the entity list maintained by the Bureau of Industry and Security of the Department of Commerce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Confronting CCP Human Rights Abusers Act .\n#### 2. Inclusion of Ministry of Public Security\u2019s Institute of Forensic Science of China on entity list\n##### (a) In general\nNot later than 60 days after the date of the enactment of this Act, the Under Secretary of Commerce for Industry and Security shall include on the entity list the Ministry of Public Security\u2019s Institute of Forensic Science of China, including the aliases\u2014\n**(1)**\nthe Forensic Identification Center of the Ministry of Public Security of the People\u2019s Republic of China; and\n**(2)**\nthe Material Identification Center of the Ministry of Public Security of the People\u2019s Republic of China.\n##### (b) Waiver\nThe President, acting through the Secretary of Commerce, may waive the application of subsection (a) if, not later than 60 days after the date of the enactment of this Act, the President submits to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a certification that the Ministry of Public Security\u2019s Institute of Forensic Science of China is not\u2014\n**(1)**\nengaging in an activity contrary to the foreign policy interests of the United States; or\n**(2)**\nimplicated in or contributing to abuse or a violation of human rights with respect to the campaign of the People\u2019s Republic of China of repression, mass arbitrary detention, forced labor, and high-technology surveillance against Uyghurs, Kazakhs, and other members of Muslim minority groups in the Xinjiang Uyghur Autonomous Region.\n##### (c) Entity list defined\nIn this section, the term entity list means the list maintained by the Bureau of Industry and Security of the Department of Commerce and set forth in Supplement No. 4 to part 744 of the Export Administration Regulations, or successor regulations.",
      "versionDate": "2025-05-15",
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
        "actionDate": "2025-05-15",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1772",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Confronting CCP Human Rights Abusers Act",
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
        "name": "International Affairs",
        "updateDate": "2025-06-20T13:52:57Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3461ih.xml"
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
      "title": "Confronting CCP Human Rights Abusers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Confronting CCP Human Rights Abusers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the inclusion of the Ministry of Public Security's Institute of Forensic Science of China on the entity list maintained by the Bureau of Industry and Security of the Department of Commerce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:23Z"
    }
  ]
}
```
