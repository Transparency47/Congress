# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1732?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1732
- Title: CHEERS Act
- Congress: 119
- Bill type: S
- Bill number: 1732
- Origin chamber: Senate
- Introduced date: 2025-05-13
- Update date: 2025-12-05T22:51:21Z
- Update date including text: 2025-12-05T22:51:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in Senate
- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-13: Introduced in Senate

## Actions

- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1732",
    "number": "1732",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "CHEERS Act",
    "type": "S",
    "updateDate": "2025-12-05T22:51:21Z",
    "updateDateIncludingText": "2025-12-05T22:51:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T18:50:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1732is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1732\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Mr. Sheehy (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to treat energy efficient kegs as efficient commercial building property for purposes of the energy efficient commercial buildings deduction.\n#### 1. Short title\nThis Act may be cited as the Creating Hospitality Economic Enhancement for Restaurants and Servers Act or the CHEERS Act .\n#### 2. Energy efficient keg property\n##### (a) In general\nSection 179D(d) of the Internal Revenue Code of 1986 is amended by inserting after paragraph (5) the following new paragraph:\n(6) Qualified energy-efficient draft property (A) In general Notwithstanding subsection (c)(1)(D), for purposes of this section, qualified energy-efficient draft property shall be treated as energy efficient commercial building property. (B) Qualified energy-efficient draft property defined For purposes of this paragraph, the term qualified energy-efficient draft property means property\u2014 (i) which meets the requirements of paragraphs (A) and (B)(i) of paragraph (1) of subsection (c), (ii) which is principally used in the conduct of a trade or business of operating a restaurant, bar, or entertainment venue, and (iii) which is a stainless steel or aluminum container or related commercial tap equipment used for the distribution and sale of alcohol. (C) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this paragraph, including regulations providing for the appropriate treatment of taxpayers that rent or lease qualified energy-efficient draft property to further such purposes. .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after the date of enactment of this Act.",
      "versionDate": "2025-05-13",
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
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3325",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CHEERS Act",
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
        "name": "Taxation",
        "updateDate": "2025-06-06T18:35:31Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1732is.xml"
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
      "title": "CHEERS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CHEERS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Creating Hospitality Economic Enhancement for Restaurants and Servers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to treat energy efficient kegs as efficient commercial building property for purposes of the energy efficient commercial buildings deduction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:40Z"
    }
  ]
}
```
