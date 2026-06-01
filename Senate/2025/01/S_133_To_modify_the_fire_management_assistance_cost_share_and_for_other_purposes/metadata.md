# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/133?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/133
- Title: Fire Suppression and Response Funding Assurance Act
- Congress: 119
- Bill type: S
- Bill number: 133
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-12-11T22:41:08Z
- Update date including text: 2025-12-11T22:41:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/133",
    "number": "133",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Fire Suppression and Response Funding Assurance Act",
    "type": "S",
    "updateDate": "2025-12-11T22:41:08Z",
    "updateDateIncludingText": "2025-12-11T22:41:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T21:06:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AK"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NM"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s133is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 133\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Padilla (for himself, Mr. Sullivan , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo modify the fire management assistance cost share, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fire Suppression and Response Funding Assurance Act .\n#### 2. Fire management assistance cost share\n##### (a) In general\nSection 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 ) is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (f); and\n**(2)**\nby inserting after subsection (d) the following:\n(e) Federal share The Federal share of assistance under this section shall be not less than 75 percent of the eligible cost of such assistance. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall only apply to amounts appropriated on or after the date of enactment of this Act.\n#### 3. Rulemaking\nNot later than 3 years after the date of enactment of this Act, the President, acting through the Administrator of the Federal Emergency Management Agency, shall conduct and complete a rulemaking to provide criteria for the circumstances under which the Administrator may recommend the President increase the Federal cost share for section 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 ).\n#### 4. Policy update\nThe Administrator of the Federal Emergency Management Agency shall update the policy for grants made under section 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 ), consistent with assistance provided under a major disaster and emergency declaration under that Act, to provide that predeployment of domestic assets by States, local, and Tribal governments may be eligible for reimbursement under such section 420.",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-12-01",
        "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management."
      },
      "number": "5652",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Wildfire Recovery Act",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-01T20:43:14Z"
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
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s133is.xml"
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
      "title": "Fire Suppression and Response Funding Assurance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fire Suppression and Response Funding Assurance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify the fire management assistance cost share, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:39Z"
    }
  ]
}
```
