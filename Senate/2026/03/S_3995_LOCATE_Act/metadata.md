# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3995?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3995
- Title: LOCATE Act
- Congress: 119
- Bill type: S
- Bill number: 3995
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-03-23T20:33:51Z
- Update date including text: 2026-03-23T20:33:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3995",
    "number": "3995",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "LOCATE Act",
    "type": "S",
    "updateDate": "2026-03-23T20:33:51Z",
    "updateDateIncludingText": "2026-03-23T20:33:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T22:52:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3995is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3995\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Luj\u00e1n introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require U.S. Customs and Border Protection and U.S. Immigration and Customs Enforcement to timely update the Online Detainee Locator System, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Location Updates for Custody and Transparency Enforcement Act or the LOCATE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Custody event**\nThe term custody event means, with respect to an individual in immigration detention, any of the following:\n**(A)**\nInitial intake or placement into custody by U.S. Customs and Border Protection or U.S. Immigration and Customs Enforcement.\n**(B)**\nTransfer from one detention facility to another detention facility.\n**(C)**\nRelease from custody.\n**(D)**\nRemoval from the United States.\n**(E)**\nDeath.\n**(F)**\nAny other significant change in status that materially affects the individual\u2019s location or custodial status.\n**(2) Online detainee locator system**\nThe term Online Detainee Locator System means the online system maintained by U.S. Immigration and Customs Enforcement for the purposes of tracking detainees in its custody or the custody of U.S. Customs and Border Protection.\n#### 3. Timely reporting of detainee custody events\n##### (a) Timely updates\nNot later than 6 hours after any custody event affecting an individual in the custody of U.S. Customs and Border Protection or not later than 12 hours after any custody event affecting an individual in the custody of U.S. Immigration and Customs Enforcement, the Online Detainee Locator System shall be updated to accurately reflect such individual\u2019s current custodial status and location.\n##### (b) Transfers between CBP and ICE\nIf an individual who was initially taken into custody by U.S. Customs and Border Protection is subsequently transferred to U.S. Immigration and Customs Enforcement, U.S. Customs and Border Protection shall provide all relevant biographical and custodial information relating to such individual to U.S. Immigration and Customs Enforcement not later than 4 hours after such transfer to facilitate timely entry into the Online Detainee Locator System.\n##### (c) Data accuracy\nThe Online Detainee Locator System shall include, for each detainee\u2014\n**(1)**\nthe full name and date of birth of the detainee;\n**(2)**\nthe current facility where the detainee is being held, including the address of such facility and the contact information for a knowledgeable official at such facility;\n**(3)**\nthe date of initial apprehension and most recent transfer of such detainee, if applicable;\n**(4)**\nany scheduled release, removal, or transfer date for such detainee, if known; and\n**(5)**\ninformation regarding the release, deportation, or death of such detainee, if applicable.\n##### (d) Rule of construction\nNothing in this section may be construed to supersede or replace any requirement that U.S. Customs and Border Protection and U.S. Immigration and Customs Enforcement report in-custody deaths in accordance with section 3 of the Death in Custody Reporting Act of 2013 ( 42 U.S.C. 13727a ).\n#### 4. Enforcement and accountability\n##### (a) Inspector General audits\nThe Inspector General of the Department of Homeland Security shall\u2014\n**(1)**\nconduct annual audits to evaluate the Department of Homeland Security's compliance with the requirements under section 3; and\n**(2)**\nsubmit annual reports to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives that summarize the findings of such audits.\n##### (b) Timely notification of family or representatives\nNot later than 12 hours after a custody event involving a detainee, reasonable efforts shall be made to notify close family members or legal representatives of such detainee, if known, of such custody event.\n#### 5. Effective date\nThis Act shall take effect on the date that is 30 days after the date of the enactment of this Act.",
      "versionDate": "2026-03-04",
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
        "name": "Immigration",
        "updateDate": "2026-03-23T20:33:51Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3995is.xml"
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
      "title": "LOCATE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LOCATE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Location Updates for Custody and Transparency Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require U.S. Customs and Border Protection and U.S. Immigration and Customs Enforcement to timely update the Online Detainee Locator System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:50Z"
    }
  ]
}
```
