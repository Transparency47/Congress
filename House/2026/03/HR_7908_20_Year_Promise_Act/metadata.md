# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7908?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7908
- Title: 20-Year Promise Act
- Congress: 119
- Bill type: HR
- Bill number: 7908
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-04-01T20:32:38Z
- Update date including text: 2026-04-01T20:32:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7908",
    "number": "7908",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "20-Year Promise Act",
    "type": "HR",
    "updateDate": "2026-04-01T20:32:38Z",
    "updateDateIncludingText": "2026-04-01T20:32:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:34:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7908ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7908\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mrs. Kiggans of Virginia introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for an additional 36 months of entitlement to educational assistance for individuals who serve 20 or more years in the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 20-Year Promise Act .\n#### 2. Additional months of entitlement to educational assistance\n##### (a) Additional months of entitlement\nSection 3312 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking (b) and (c) and inserting (b), (c), and (d) ; and\n**(2)**\nby adding at the end the following new subsection:\n(d) Additional months of entitlement for certain individuals Notwithstanding section 3695 of this title, an individual entitled to educational assistance under this chapter who serves an aggregate of 20 or more years in the Armed Forces, without regard to duty status, is entitled to a number of months of educational assistance under section 3313 of this title equal to 72 months. .\n##### (b) Transfer of additional months of entitlement\nSubsection (d) of section 3319 of such title is amended by striking 36 months and inserting 72 months for an individual eligible for additional months of entitlement under section 3312(d) of this title, and 36 months for all other individuals .\n##### (c) Limitation on period of assistance under two of more programs\nSection 3695 of such title is amended by adding at the end the following new subsection:\n(d) The limitation in subsection (a) shall not apply to any individual eligible for additional months of entitlement under section 3312(d) of this title. .\n##### (d) Applicability\nThe amendments made by this Act shall apply with respect to an individual who, on or after the date of the enactment of this Act, completes an aggregate of 20 or more years of service in the Armed Forces, without regard to\u2014\n**(1)**\nduty status; or\n**(2)**\nwhen such individual joined the Armed Forces.",
      "versionDate": "2026-03-12",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-01T20:32:38Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7908ih.xml"
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
      "title": "20-Year Promise Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "20-Year Promise Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-28T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for an additional 36 months of entitlement to educational assistance for individuals who serve 20 or more years in the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T04:48:21Z"
    }
  ]
}
```
