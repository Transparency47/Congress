# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2242?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2242
- Title: Counternarcotics Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 2242
- Origin chamber: Senate
- Introduced date: 2025-07-10
- Update date: 2025-10-01T01:04:27Z
- Update date including text: 2025-10-01T01:04:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in Senate
- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.
- Latest action: 2025-07-10: Introduced in Senate

## Actions

- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2242",
    "number": "2242",
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
    "title": "Counternarcotics Enhancement Act",
    "type": "S",
    "updateDate": "2025-10-01T01:04:27Z",
    "updateDateIncludingText": "2025-10-01T01:04:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Intelligence (Select) Committee",
          "systemCode": "slin00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Select Committee on Intelligence.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:17:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Intelligence (Select) Committee",
      "systemCode": "slin00",
      "type": "Select"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2242is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2242\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mr. Cornyn (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Select Committee on Intelligence\nA BILL\nTo require the Director of National Intelligence to submit an action plan to enhance counternarcotics collaboration, coordination, and cooperation with the Government of Mexico, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Counternarcotics Enhancement Act .\n#### 2. Plan to enhance counternarcotics collaboration, coordination, and cooperation with the Government of Mexico\n##### (a) Requirement for intelligence community elements\nNot later than 60 days after the date of the enactment of this Act, the head of each element of the intelligence community shall submit to the Director of National Intelligence the following:\n**(1)**\nA description and assessment of the intelligence community element\u2019s direct relationship, if any, with any element of the Government of Mexico, including an assessment of the counterintelligence risks of such relationship.\n**(2)**\nA strategy to enhance counternarcotics cooperation and appropriate coordination with each element of the Government of Mexico with which the intelligence community element has a direct relationship.\n**(3)**\nRecommendations and a description of the resources required to efficiently and effectively implement the strategy required by paragraph (2) in furtherance of the national interest of the United States.\n##### (b) Requirement for Director of National Intelligence\nNot later than 180 days after the date of the enactment of this Act, the Director of National Intelligence shall submit to the congressional intelligence committees the following:\n**(1)**\nThe submissions received by the Director pursuant to subsection (a).\n**(2)**\nAn action plan to enhance counternarcotics collaboration, coordination, and cooperation with the Government of Mexico, including recommendations or requests for any changes in authorities or resources in order to effectuate the plan effectively in fiscal year 2026.\n##### (c) Form\n**(1) Submissions from intelligence community elements**\nThe submissions required by subsection (b)(1) shall be submitted to the congressional intelligence committees in the same form in which they were submitted to the Director of National Intelligence.\n**(2) Action plan**\nThe submission required by subsection (b)(2) shall be submitted in unclassified form, but may include a classified annex.\n##### (d) Congressional intelligence committees defined\nIn this section, the term congressional intelligence committees has the meaning given that term in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 ).",
      "versionDate": "2025-07-10",
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
        "actionDate": "2025-07-29",
        "text": "By Senator Cotton from Select Committee on Intelligence filed written report. Report No. 119-51. Minority views filed."
      },
      "number": "2342",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Intelligence Authorization Act for Fiscal Year 2026",
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
        "updateDate": "2025-07-29T21:12:37Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2242is.xml"
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
      "title": "Counternarcotics Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Counternarcotics Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of National Intelligence to submit an action plan to enhance counternarcotics collaboration, coordination, and cooperation with the Government of Mexico, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:33:24Z"
    }
  ]
}
```
