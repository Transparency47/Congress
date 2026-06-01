# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5896?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5896
- Title: GRID Act
- Congress: 119
- Bill type: HR
- Bill number: 5896
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-04-10T12:42:11Z
- Update date including text: 2026-04-10T12:42:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5896",
    "number": "5896",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "GRID Act",
    "type": "HR",
    "updateDate": "2026-04-10T12:42:11Z",
    "updateDateIncludingText": "2026-04-10T12:42:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5896ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5896\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to repeal the standard relating to electric vehicle charging programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarding Ratepayers from Imposed EV Charging Directives Act or the GRID Act .\n#### 2. Repeal of standard relating to electric vehicle charging programs\n##### (a) Standard\nParagraph (21) of section 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d) ) is repealed.\n##### (b) Conforming amendments\n**(1) Time limitations**\nParagraph (8) of section 112(b) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622(b) ) is repealed.\n**(2) Failure to comply**\nSection 112(c) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622(c) ) is amended by striking In the case of the standard established by paragraph (21) of section 111(d), the reference contained in this subsection to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of that paragraph (21). .\n**(3) Other prior State actions**\nSubsection (h) of section 112 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622 ) is repealed.\n**(4) Prior and pending proceedings**\nSection 124 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2634 ) is amended by striking In the case of the standard established by paragraph (21) of section 111(d), the reference contained in this section to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of that paragraph (21). .",
      "versionDate": "2025-10-31",
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
        "name": "Energy",
        "updateDate": "2026-04-10T12:42:11Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5896ih.xml"
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
      "title": "GRID Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GRID Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guarding Ratepayers from Imposed EV Charging Directives Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to repeal the standard relating to electric vehicle charging programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T12:18:14Z"
    }
  ]
}
```
