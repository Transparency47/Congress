# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4580?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4580
- Title: No Tax on Border Patrol Agent Overtime Act
- Congress: 119
- Bill type: S
- Bill number: 4580
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-29T07:23:31Z
- Update date including text: 2026-05-29T07:23:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4580",
    "number": "4580",
    "originChamber": "Senate",
    "policyArea": {},
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
    "title": "No Tax on Border Patrol Agent Overtime Act",
    "type": "S",
    "updateDate": "2026-05-29T07:23:31Z",
    "updateDateIncludingText": "2026-05-29T07:23:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
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
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T15:19:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4580is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4580\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Cornyn introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide that overtime pay provided to certain border patrol agents is qualified overtime compensation.\n#### 1. Short title\nThis Act may be cited as the No Tax on Border Patrol Agent Overtime Act .\n#### 2. Qualified overtime compensation for border patrol agents\n##### (a) In general\nSection 225(c)(1) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) In general For purposes of this section, the term qualified overtime compensation means\u2014 (A) overtime compensation paid to an individual required under section 7 of the Fair Labor Standards Act of 1938 that is in excess of the regular rate (as used in such section) at which such individual is employed, or (B) amounts paid to a border patrol agent (as defined in subsection (a) of section 5550 of title 5, United States Code), other than the hazardous duty pay payable under subsection (c)(3) of such section, that are in excess of the rate of basic pay that would be in effect for such border patrol agent if the rate of basic pay of such border patrol agent were determined without regard to such section, including\u2014 (i) the supplemental pay described in subsection (b)(2) of such section, (ii) the supplemental pay described in subsection (b)(3) of such section, (iii) premium pay payable under subsection (c)(1) of such section, and (iv) pay for overtime work payable under section 5542(g) of such title. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-05-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4580is.xml"
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
      "title": "No Tax on Border Patrol Agent Overtime Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:23:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Tax on Border Patrol Agent Overtime Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide that overtime pay provided to certain border patrol agents is qualified overtime compensation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:18:35Z"
    }
  ]
}
```
