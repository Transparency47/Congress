# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6441?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6441
- Title: Puerto Rico Postal Equity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6441
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-04-17T08:07:16Z
- Update date including text: 2026-04-17T08:07:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6441",
    "number": "6441",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001103",
        "district": "",
        "firstName": "Pablo",
        "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
        "lastName": "Hern\u00e1ndez",
        "party": "D",
        "state": "PR"
      }
    ],
    "title": "Puerto Rico Postal Equity Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:16Z",
    "updateDateIncludingText": "2026-04-17T08:07:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:07:50Z",
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
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6441ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6441\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Hern\u00e1ndez introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the Postmaster General update the systems of the Postal Service to accurately recognize and preserve address data, including the proper use of linguistic characters and place names, in Puerto Rico, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Puerto Rico Postal Equity Act of 2025 .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nThe accurate identification, formatting, and integration of physical addresses are essential to the efficient operation of the United States Postal Service, the reliability of mail delivery, the facilitation of e-commerce, and the equitable distribution of Federal programs and services.\n**(2)**\nHistorical and structural complexities in Puerto Rico\u2019s local addressing conventions create inconsistencies between locally assigned addresses and those recognized by the United States Postal Service, Federal agencies, and major private platforms, resulting in recurring delivery and validation failures.\n**(3)**\nSuch inconsistencies include the omission or alteration of diacritical marks recognized in Spanish-language place names, street names, and surnames, which can lead to misidentification, delivery errors, and data mismatches in official records.\n**(4)**\nThe preservation of accurate orthography and culturally specific characters in Federal data systems is essential to ensuring the integrity of official records, compliance with civil rights and language access standards, and the protection of identity and property rights.\n**(5)**\nStrengthened coordination between the United States Postal Service and the Department of Commerce, including the Census Bureau, would enhance national data accuracy, support economic development, and advance equity across Puerto Rico by improving how the United States Postal Service identifies and resolves recurrent address recognition and delivery issues in Puerto Rico.\n#### 3. Improvements to accuracy of Puerto Rico address data\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Postmaster General shall develop and implement improvements to the systems of the United States Postal Service to improve the accuracy and recognition of addresses in Puerto Rico, including\u2014\n**(1)**\nusing existing operational indicators of the United States Postal Service, including Undeliverable-As-Addressed codes, mail delivery exception records, address quality data from the address management system of the United States Postal Service, delivery point validation results, consumer complaint information, and address validation outcomes data from the websites of the United States Postal Service, to identify locations in Puerto Rico with persistent address recognition or mail delivery issues;\n**(2)**\nupdating the address records, routing information, and validation tables of the United States Postal Service for the locations identified under subsection (1);\n**(3)**\nrevising the relevant systems of the United States Postal Service, including address matching, address validation, and mail and delivery routing systems, to support the use of diacritical marks and other address elements used in Puerto Rico for addresses in Puerto Rico; and\n**(4)**\ntaking such other actions as determined appropriate by the Postmaster General based on the relevant data to improve the recognition by the systems of the United States Postal Service of and the proper delivery of mail to properly assigned addresses in Puerto Rico.\n##### (b) Consultation\nIn carrying out subsection (a), the Postmaster General shall consult with the Bureau of the Census, including the Census Open Innovation Lab, the Puerto Rico Planning Board established by Puerto Rico Act 75\u20131975 (23 L.P.R.A. 62 et seq.), and appropriate local governments in Puerto Rico, to obtain information required to carry out such subsection.\n##### (c) Reporting\nNot later than one year after enactment of this Act, and annually thereafter for three years, the Postmaster General shall submit to Congress a report detailing\u2014\n**(1)**\nthe actions taken under this section;\n**(2)**\nthe progress of the United States Postal Service in improving the recognition of and accuracy of delivery to addresses in Puerto Rico; and\n**(3)**\nany barriers to carrying out subsection (a) and recommendations for legislative or administrative action to address such barriers.\n##### (d) Diacritical mark defined\nIn this Act, the term diacritical mark means any accent, tilde, or other orthographic sign used by the Spanish language to indicate pronunciation or meaning in proper nouns and place names within Puerto Rico.\n#### 4. Cutgo compliance\nNo additional amounts are authorized to be appropriated to carry out this Act. The Postmaster General shall carry out this Act using amounts otherwise appropriated or made available to United States Postal Service.",
      "versionDate": "2025-12-04",
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
        "updateDate": "2026-01-06T22:01:34Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6441ih.xml"
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
      "title": "Puerto Rico Postal Equity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T11:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Puerto Rico Postal Equity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Postmaster General update the systems of the Postal Service to accurately recognize and preserve address data, including the proper use of linguistic characters and place names, in Puerto Rico, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T11:18:28Z"
    }
  ]
}
```
