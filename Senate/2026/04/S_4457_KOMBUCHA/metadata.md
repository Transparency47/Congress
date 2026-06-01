# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4457?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4457
- Title: KOMBUCHA
- Congress: 119
- Bill type: S
- Bill number: 4457
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-13T15:55:09Z
- Update date including text: 2026-05-13T15:55:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4457",
    "number": "4457",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "KOMBUCHA",
    "type": "S",
    "updateDate": "2026-05-13T15:55:09Z",
    "updateDateIncludingText": "2026-05-13T15:55:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T17:17:56Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4457is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4457\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Wyden introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to ensure that low alcohol by volume kombucha is exempt from any excise taxes and any regulations under chapter 53 of such Code which are imposed on alcoholic beverages.\n#### 1. Short title\nThis Act may be cited as the Keeping Our Manufacturers from Being Unfairly taxed while Championing Health Act or KOMBUCHA .\n#### 2. Tax-free production of low alcohol by volume kombucha\n##### (a) Exemption from tax on wine\nSection 5042(a) of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(4) Low alcohol by volume kombucha (A) In general Subject to regulations prescribed by the Secretary, low alcohol by volume kombucha shall not be subject to\u2014 (i) tax as wine, or (ii) the provisions of subchapter F. (B) Definition For purposes of this chapter, the term low alcohol by volume kombucha means a beverage which\u2014 (i) is fermented solely by a symbiotic culture of bacteria and yeast, (ii) contains not more than 1.25 percent of alcohol by volume, (iii) is sold or offered for sale as kombucha, and (iv) is derived from\u2014 (I) fermentable sugars, including sugar, malt or malt substitute, honey, and fruit juice, and (II) plant materials, including tea and coffee. .\n##### (b) Exemption from tax on beer\nSection 5053 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby redesignating subsection (i) as subsection (j), and\n**(2)**\nby inserting after subsection (h) the following new subsection:\n(i) Production of low alcohol by volume kombucha Subject to regulations prescribed by the Secretary, low alcohol by volume kombucha (as defined in section 5042(a)(4)(B)) shall not be subject to\u2014 (1) tax as beer, or (2) the provisions of subchapter G. .\n##### (c) Effective date\nThe amendments made by this section shall apply to calendar quarters beginning after the date of enactment of this Act.",
      "versionDate": "2026-04-30",
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
        "actionDate": "2026-04-30",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "8631",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "KOMBUCHA",
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
        "updateDate": "2026-05-13T15:55:09Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4457is.xml"
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
      "title": "KOMBUCHA",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "KOMBUCHA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keeping Our Manufacturers from Being Unfairly taxed while Championing Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to ensure that low alcohol by volume kombucha is exempt from any excise taxes and any regulations under chapter 53 of such Code which are imposed on alcoholic beverages.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:31Z"
    }
  ]
}
```
