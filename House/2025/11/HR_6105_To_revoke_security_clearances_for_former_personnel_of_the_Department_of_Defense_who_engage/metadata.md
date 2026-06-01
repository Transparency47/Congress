# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6105?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6105
- Title: REVOKE Act
- Congress: 119
- Bill type: HR
- Bill number: 6105
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-03-27T08:06:28Z
- Update date including text: 2026-03-27T08:06:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6105",
    "number": "6105",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "REVOKE Act",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:28Z",
    "updateDateIncludingText": "2026-03-27T08:06:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NC"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6105ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6105\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Pfluger (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo revoke security clearances for former personnel of the Department of Defense who engage in lobbying activities on behalf of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restricting Ex-Vetted Officials from Knowledge Exploitation Act or the REVOKE Act .\n#### 2. Revocation of Security Clearances for Certain Persons\n##### (a) Prohibition\nNotwithstanding any other provision of law, the Secretary of Defense shall suspend or revoke a security clearance or eligibility for access to classified information for any retired or separated member of the Armed Forces or civilian employee of the Department of Defense who engages in an activity described in subsection (b).\n##### (b) Activities described\nThe activities described in this subsection are lobbying activities or lobbying contacts for or on behalf of any entity that is\u2014\n**(1)**\nidentified by the Secretary of Defense in the most recent report submitted under section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 10 U.S.C. 113 note) as a Chinese military company; and\n**(2)**\nincluded in the Non-SDN Chinese Military-Industrial Complex Companies List published by the Department of the Treasury.\n##### (c) Waiver\nThe Secretary of Defense may, for periods not to exceed 180 days, waive the application of the prohibition in subsection (a) for an individual if the Secretary certifies to the congressional defense committees that doing so is in the national security interest of the United States.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term congressional defense committees has the meaning given the term in section 101(a) of title 10, United States Code.\n**(2)**\nThe term lobbying activities has the meaning given such term in section 3 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602 ).\n**(3)**\nThe term lobbying contact has the meaning given such term in section 3 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602 ), except that clause (iv) of paragraph (8)(B)(iv) of such section shall not apply.",
      "versionDate": "2025-11-18",
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
        "actionDate": "2025-11-18",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "3181",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "REVOKE Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-03T21:32:30Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6105ih.xml"
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
      "title": "REVOKE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T10:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REVOKE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T10:23:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restricting Ex-Vetted Officials from Knowledge Exploitation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T10:23:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To revoke security clearances for former personnel of the Department of Defense who engage in lobbying activities on behalf of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T10:18:32Z"
    }
  ]
}
```
