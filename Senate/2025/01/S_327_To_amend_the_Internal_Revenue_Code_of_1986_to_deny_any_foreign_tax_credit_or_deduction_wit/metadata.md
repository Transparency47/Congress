# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/327?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/327
- Title: HONOR Act
- Congress: 119
- Bill type: S
- Bill number: 327
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2026-04-17T15:15:27Z
- Update date including text: 2026-04-17T15:15:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2026-03-10 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S953; text: CR S953)
- 2026-03-10 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-03-10 - Discharge: Senate Committee on Finance discharged by Unanimous Consent.
- 2026-03-10 - Committee: Senate Committee on Finance discharged by Unanimous Consent.
- 2026-03-16 - Floor: Message on Senate action sent to the House.
- 2026-03-16 15:00:31 - Floor: Received in the House.
- 2026-03-16 15:05:55 - Floor: Held at the desk.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2026-03-10 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S953; text: CR S953)
- 2026-03-10 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-03-10 - Discharge: Senate Committee on Finance discharged by Unanimous Consent.
- 2026-03-10 - Committee: Senate Committee on Finance discharged by Unanimous Consent.
- 2026-03-16 - Floor: Message on Senate action sent to the House.
- 2026-03-16 15:00:31 - Floor: Received in the House.
- 2026-03-16 15:05:55 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/327",
    "number": "327",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "HONOR Act",
    "type": "S",
    "updateDate": "2026-04-17T15:15:27Z",
    "updateDateIncludingText": "2026-04-17T15:15:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-03-16",
      "actionTime": "15:05:55",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-03-16",
      "actionTime": "15:00:31",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S953; text: CR S953)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-10",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Finance discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-03-10",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Finance discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-30",
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
      "actionDate": "2025-01-30",
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
        "item": [
          {
            "date": "2026-03-10T21:07:10Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-01-30T17:38:27Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s327is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 327\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Ms. Cortez Masto (for herself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny any foreign tax credit or deduction with respect to taxes paid or accrued to the Russian Federation.\n#### 1. Short title\nThis Act may be cited as the Hindering Oppressive Nations from Obtaining Revenue Act or HONOR Act .\n#### 2. Denial of foreign tax credit with respect to the Russian Federation\n##### (a) In general\nSection 901(j)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Special rule for Russia (i) In general This subsection shall apply to the Russian Federation during the period described in clause (ii). (ii) Period of application The period described in this clause with respect to any country is the period\u2014 (I) beginning on the date that is 30 days after the date of the enactment of this subparagraph, and (II) ending on the date on which the resumption of the application of the rates of duty set forth in column 1 of the Harmonized Tariff Schedule of the United States to products of that country takes effect pursuant to section 4(b) of the Suspending Normal Trade Relations with Russia and Belarus Act. .\n##### (b) Deduction denied\nSection 901(j)(3) of such Code is amended by adding at the end the following new sentence: The preceding sentence shall not apply to any tax of any country to which paragraph (2)(C) applies. .\n##### (c) Effective dates\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall take effect on the date of the enactment of this Act.\n**(2) Deduction limitation**\nThe amendment made by subsection (b) shall apply to taxes paid or accrued (or deemed paid or accrued under section 960 of the Internal Revenue Code of 1986) after the date that is 90 days after the date of the enactment of this Act.\n**(3) Nonapplication of treaty rules**\nThis section and the amendments made by this section shall be applied without regard to any treaty obligation of the United States.",
      "versionDate": "2025-01-30",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s327es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 327\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Internal Revenue Code of 1986 to deny any foreign tax credit or deduction with respect to taxes paid or accrued to the Russian Federation.\n#### 1. Short title\nThis Act may be cited as the Hindering Oppressive Nations from Obtaining Revenue Act or HONOR Act .\n#### 2. Denial of foreign tax credit with respect to the Russian Federation\n##### (a) In general\nSection 901(j)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Special rule for Russia (i) In general This subsection shall apply to the Russian Federation during the period described in clause (ii). (ii) Period of application The period described in this clause with respect to any country is the period\u2014 (I) beginning on the date that is 30 days after the date of the enactment of this subparagraph, and (II) ending on the date on which the resumption of the application of the rates of duty set forth in column 1 of the Harmonized Tariff Schedule of the United States to products of that country takes effect pursuant to section 4(b) of the Suspending Normal Trade Relations with Russia and Belarus Act. .\n##### (b) Deduction denied\nSection 901(j)(3) of such Code is amended by adding at the end the following new sentence: The preceding sentence shall not apply to any tax of any country to which paragraph (2)(C) applies. .\n##### (c) Effective dates\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall take effect on the date of the enactment of this Act.\n**(2) Deduction limitation**\nThe amendment made by subsection (b) shall apply to taxes paid or accrued (or deemed paid or accrued under section 960 of the Internal Revenue Code of 1986) after the date that is 90 days after the date of the enactment of this Act.\n**(3) Nonapplication of treaty rules**\nThis section and the amendments made by this section shall be applied without regard to any treaty obligation of the United States.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-03-11T14:13:09Z"
          },
          {
            "name": "Europe",
            "updateDate": "2026-03-11T14:13:17Z"
          },
          {
            "name": "Income tax credits",
            "updateDate": "2026-03-11T14:13:25Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2026-03-11T14:13:31Z"
          },
          {
            "name": "Russia",
            "updateDate": "2026-03-11T14:13:45Z"
          },
          {
            "name": "Tariffs",
            "updateDate": "2026-03-11T14:13:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-04-28T21:58:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s327",
          "measure-number": "327",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2026-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s327v00",
            "update-date": "2026-04-17"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Hindering Oppressive Nations from Obtaining Revenue Act or HONOR Act</strong></p><p>This bill prohibits a taxpayer from claiming the foreign tax credit (FTC) or an itemized tax deduction for taxes paid, accrued, or deemed paid to Russia.</p><p>Under current law, a taxpayer may claim the FTC for income, war profits, and excess profits taxes (or taxes imposed in lieu of these taxes) paid, accrued, or deemed paid to a foreign country (and certain U.S. possessions) or an itemized tax deduction for such taxes, both subject to limitations.</p><p>However, under current law, a taxpayer may not claim the FTC (but may claim an itemized tax deduction) for taxes paid to a foreign country if (1) the United States does not recognize the country\u2019s government, (2) the United States severs or does not conduct diplomatic relations with the country, or (3) the country is designated by the Department of State as supporting international terrorist acts. (Currently, the FTC is disallowed for taxes paid, accrued, or deemed paid to Iran, North Korea, Sudan, and Syria.)</p><p>Under the bill, a taxpayer may not claim the FTC for taxes paid, accrued, or deemed paid to Russia beginning 30 days after the date of enactment and until normal U.S. trade relations with Russia are restored (pursuant to requirements established by the Suspending Normal Trade Relations with Russia and Belarus Act).</p><p>The bill also disallows an itemized tax deduction for taxes paid, accrued, or deemed to be paid to Russia (effective 90 days after the date of enactment).</p>"
        },
        "title": "HONOR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s327.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Hindering Oppressive Nations from Obtaining Revenue Act or HONOR Act</strong></p><p>This bill prohibits a taxpayer from claiming the foreign tax credit (FTC) or an itemized tax deduction for taxes paid, accrued, or deemed paid to Russia.</p><p>Under current law, a taxpayer may claim the FTC for income, war profits, and excess profits taxes (or taxes imposed in lieu of these taxes) paid, accrued, or deemed paid to a foreign country (and certain U.S. possessions) or an itemized tax deduction for such taxes, both subject to limitations.</p><p>However, under current law, a taxpayer may not claim the FTC (but may claim an itemized tax deduction) for taxes paid to a foreign country if (1) the United States does not recognize the country\u2019s government, (2) the United States severs or does not conduct diplomatic relations with the country, or (3) the country is designated by the Department of State as supporting international terrorist acts. (Currently, the FTC is disallowed for taxes paid, accrued, or deemed paid to Iran, North Korea, Sudan, and Syria.)</p><p>Under the bill, a taxpayer may not claim the FTC for taxes paid, accrued, or deemed paid to Russia beginning 30 days after the date of enactment and until normal U.S. trade relations with Russia are restored (pursuant to requirements established by the Suspending Normal Trade Relations with Russia and Belarus Act).</p><p>The bill also disallows an itemized tax deduction for taxes paid, accrued, or deemed to be paid to Russia (effective 90 days after the date of enactment).</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s327"
    },
    "title": "HONOR Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Hindering Oppressive Nations from Obtaining Revenue Act or HONOR Act</strong></p><p>This bill prohibits a taxpayer from claiming the foreign tax credit (FTC) or an itemized tax deduction for taxes paid, accrued, or deemed paid to Russia.</p><p>Under current law, a taxpayer may claim the FTC for income, war profits, and excess profits taxes (or taxes imposed in lieu of these taxes) paid, accrued, or deemed paid to a foreign country (and certain U.S. possessions) or an itemized tax deduction for such taxes, both subject to limitations.</p><p>However, under current law, a taxpayer may not claim the FTC (but may claim an itemized tax deduction) for taxes paid to a foreign country if (1) the United States does not recognize the country\u2019s government, (2) the United States severs or does not conduct diplomatic relations with the country, or (3) the country is designated by the Department of State as supporting international terrorist acts. (Currently, the FTC is disallowed for taxes paid, accrued, or deemed paid to Iran, North Korea, Sudan, and Syria.)</p><p>Under the bill, a taxpayer may not claim the FTC for taxes paid, accrued, or deemed paid to Russia beginning 30 days after the date of enactment and until normal U.S. trade relations with Russia are restored (pursuant to requirements established by the Suspending Normal Trade Relations with Russia and Belarus Act).</p><p>The bill also disallows an itemized tax deduction for taxes paid, accrued, or deemed to be paid to Russia (effective 90 days after the date of enactment).</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s327"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s327is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s327es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "HONOR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T11:03:20Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "HONOR Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-03-11T03:38:26Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Hindering Oppressive Nations from Obtaining Revenue Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-03-11T03:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HONOR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hindering Oppressive Nations from Obtaining Revenue Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to deny any foreign tax credit or deduction with respect to taxes paid or accrued to the Russian Federation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:21Z"
    }
  ]
}
```
