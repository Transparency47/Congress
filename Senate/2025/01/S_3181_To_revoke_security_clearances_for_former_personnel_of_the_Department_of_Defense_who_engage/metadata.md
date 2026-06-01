# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3181?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3181
- Title: REVOKE Act
- Congress: 119
- Bill type: S
- Bill number: 3181
- Origin chamber: Senate
- Introduced date: 2025-11-18
- Update date: 2025-12-10T07:06:26Z
- Update date including text: 2025-12-10T07:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in Senate
- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-11-18: Introduced in Senate

## Actions

- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3181",
    "number": "3181",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "REVOKE Act",
    "type": "S",
    "updateDate": "2025-12-10T07:06:26Z",
    "updateDateIncludingText": "2025-12-10T07:06:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T21:36:13Z",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3181is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3181\nIN THE SENATE OF THE UNITED STATES\nNovember 18, 2025 Mr. Cornyn (for himself and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo revoke security clearances for former personnel of the Department of Defense who engage in lobbying activities on behalf of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restricting Ex-Vetted Officials from Knowledge Exploitation Act or the REVOKE Act .\n#### 2. Revocation of Security Clearances for Certain Persons\n##### (a) Prohibition\nNotwithstanding any other provision of law, the Secretary of Defense shall suspend or revoke a security clearance or eligibility for access to classified information for any retired or separated member of the Armed Forces or civilian employee of the Department of Defense who engages in an activity described in subsection (b).\n##### (b) Activities described\nThe activities described in this subsection are lobbying activities or lobbying contacts for or on behalf of any entity that is\u2014\n**(1)**\nidentified by the Secretary of Defense in the most recent report submitted under section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 (10 U.S.C. 113 note) as a Chinese military company; and\n**(2)**\nincluded in the Non-SDN Chinese Military-Industrial Complex Companies List published by the Department of the Treasury.\n##### (c) Waiver\nThe Secretary of Defense may, for periods not to exceed 180 days, waive the application of the prohibition in subsection (a) for an individual if the Secretary certifies to the congressional defense committees that doing so is in the national security interest of the United States.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term congressional defense committees has the meaning given the term in section 101(a) of title 10, United States Code.\n**(2)**\nThe term lobbying activities has the meaning given such term in section 3 of the Lobbying Disclosure Act of 1995 (2 U.S.C. 1602).\n**(3)**\nThe term lobbying contact has the meaning given such term in section 3 of the Lobbying Disclosure Act of 1995 (2 U.S.C. 1602), except that clause (iv) of paragraph (8)(B)(iv) of such section shall not apply.",
      "versionDate": "",
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
        "actionDate": "2025-11-18",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "6105",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "REVOKE Act",
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
        "updateDate": "2025-12-05T16:13:53Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3181is.xml"
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
      "title": "REVOKE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REVOKE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restricting Ex-Vetted Officials from Knowledge Exploitation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to revoke security clearances for former personnel of the Department of Defense who engage in lobbying activities on behalf of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-05T04:03:52Z"
    }
  ]
}
```
