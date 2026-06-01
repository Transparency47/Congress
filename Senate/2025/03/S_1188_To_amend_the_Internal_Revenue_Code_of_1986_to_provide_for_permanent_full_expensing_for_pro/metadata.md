# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1188?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1188
- Title: FLARE Act
- Congress: 119
- Bill type: S
- Bill number: 1188
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2025-05-09T16:06:21Z
- Update date including text: 2025-05-09T16:06:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1188",
    "number": "1188",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "FLARE Act",
    "type": "S",
    "updateDate": "2025-05-09T16:06:21Z",
    "updateDateIncludingText": "2025-05-09T16:06:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T19:28:11Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1188is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1188\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Cruz introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for permanent full expensing for property used to capture gas that would otherwise be flared or vented and to use such gas in value-added products.\n#### 1. Short title\nThis Act may be cited as the Facilitating Lower Atmospheric Released Emissions Act or the FLARE Act .\n#### 2. Permanent full expensing of costs related to flaring and venting mitigation systems\n##### (a) In general\nSection 168(k) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(11) Permanent expensing of costs related to flaring and venting mitigation systems (A) In general In the case of any applicable energy property\u2014 (i) paragraph (8) shall not apply, and (ii) the applicable percentage shall be 100 percent. (B) Applicable energy property (i) In general For purposes of this paragraph, the term applicable energy property means any qualified property (as determined as if clause (iii) of paragraph (2)(A) did not apply with respect to such property) which is a flaring and venting mitigation system. (ii) Flaring and venting mitigation system For purposes of this subparagraph, the term flaring and venting mitigation system means a system which\u2014 (I) intakes natural gas, and (II) separates, collects, utilizes, or combusts methane and heavier hydrocarbons by\u2014 (aa) compressing or liquefying gas for use as fuel or transport to a processing facility, (bb) production of petrochemicals or fertilizer, (cc) conversion to liquid fuels, (dd) conversion to electricity for electricity-driven activities or supply to the electrical grid, (ee) conversion to computational power, (ff) mining for digital assets, or (gg) powering other oilfield equipment. (C) Foreign entity of concern (i) In general This paragraph shall not apply to any property placed in service by any foreign entity of concern. (ii) Definition In this paragraph, the term foreign entity of concern has the meaning given that term in section 10612(a) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19221(a) ). .\n##### (b) Conforming amendment\nSection 168(k)(6)(A) of the Internal Revenue Code of 1986 is amended by inserting or paragraph (11) after this paragraph .\n##### (c) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2025.",
      "versionDate": "2025-03-27",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-09T16:06:21Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1188is.xml"
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
      "title": "FLARE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FLARE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Facilitating Lower Atmospheric Released Emissions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide for permanent full expensing for property used to capture gas that would otherwise be flared or vented and to use such gas in value-added products.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T03:03:26Z"
    }
  ]
}
```
