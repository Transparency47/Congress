# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1632?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1632
- Title: Defense Workforce Integration Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1632
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-12-05T21:59:42Z
- Update date including text: 2025-12-05T21:59:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1632",
    "number": "1632",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Defense Workforce Integration Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:59:42Z",
    "updateDateIncludingText": "2025-12-05T21:59:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
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
        "item": {
          "date": "2025-05-07T18:40:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "SD"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "ND"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "VA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-07",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1632is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1632\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mrs. Shaheen (for herself, Mr. Rounds , Mr. Cramer , Mr. Kaine , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide for greater defense workforce integration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Defense Workforce Integration Act of 2025 .\n#### 2. Integration of military and civilian hiring processes\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense, in coordination with the Secretaries concerned shall establish a pathway for medically disqualified entry-level service members to enter civilian positions for which they are qualified in the Department of Defense or any of its components.\n##### (b) Air Force DRIVE program\nThe Air Force\u2019s Develop, Redistribute, Improve, Vault, Expose (DRIVE) program shall be considered sufficient to meet the requirements of subsection (a) and may, but need not, serve as a baseline from which the other military departments design their programs.\n##### (c) Entry-Level service member defined\nIn this section, the term entry-level service member means a regular or reserve member of the Armed Forces who is currently attending or has military orders to attend within 90 days\u2014\n**(1)**\nbasic training;\n**(2)**\na technical school of the Armed Forces;\n**(3)**\na service academy;\n**(4)**\nthe Reserve Officer Training Corps (ROTC); or\n**(5)**\nan officer accession program, including officer candidate school, officer training school, officer development school, or equivalent program.\n#### 3. Provision of information on career opportunities in the defense industrial base to persons ineligible for military service\nChapter 50 of title 10, United States Code, is amended by adding at the end the following new section:\n996. Provision of information on career opportunities in the defense industrial base to persons medically disqualified for military service (a) Establishment The Secretary of Defense shall establish and implement a program to provide individuals who are not medically qualified for military service with information on employment opportunities in the defense industrial base or other employment opportunities in support of the national interests of the United States. (b) Program The program established under subsection (a) shall inform and refer persons described in subsection (a) to employment, apprenticeship, and training opportunities in\u2014 (1) the defense industrial base; (2) cybersecurity or intelligence support roles; (3) research and development in defense technologies; (4) national emergency and disaster preparedness; or (5) any other non-military opportunity the Secretary considers in the national interests of the United States. (c) Collaboration The Secretary of Defense shall consult with entities in the defense industrial base, other Federal agencies, and academic institutions to carry out this section. .\n#### 4. Provision to Navy personnel of information on career opportunities at Military Sealift Command\nThe Secretary of the Navy shall provide information about career opportunities at Military Sealift Command and workforce training programs for shipbuilders to all Navy personnel as part of the Transition Assistance Program process.\n#### 5. Report\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense shall submit to the Committees on Armed Services of the Senate and the House of Representatives a report describing implementation of the requirements under sections 2 and 4 of this Act and section 996 of title 10, United States Code, as added by section 3 of this Act.",
      "versionDate": "2025-05-07",
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-07",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "3241",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Defense Workforce Integration Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-11T14:48:00Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1632is.xml"
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
      "title": "Defense Workforce Integration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Defense Workforce Integration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for greater defense workforce integration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:42Z"
    }
  ]
}
```
