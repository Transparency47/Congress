# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1345?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1345
- Title: America's First Fuels Act
- Congress: 119
- Bill type: S
- Bill number: 1345
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-01-30T14:58:23Z
- Update date including text: 2026-01-30T14:58:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1345",
    "number": "1345",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "America's First Fuels Act",
    "type": "S",
    "updateDate": "2026-01-30T14:58:23Z",
    "updateDateIncludingText": "2026-01-30T14:58:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T20:03:10Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ME"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NH"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NH"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1345is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1345\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. King (for himself, Ms. Collins , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the limitation on the credit for biomass stoves and boilers and to include biomass heating appliances in the energy credit.\n#### 1. Short title\nThis Act may be cited as the America's First Fuels Act .\n#### 2. Increased limitation for biomass stoves and boilers under energy efficient home improvement credit\n##### (a) In general\nSection 25C(b)(5) of the Internal Revenue Code of 1986 is amended by striking shall not, in the aggregate, exceed and all that follows and inserting the following:\nshall not exceed\u2014 (A) with respect to amounts paid or incurred, in the aggregate, for property described in clauses (i) and (ii) of subsection (d)(2)(A), $2,000, and (B) with respect to amounts paid or incurred, in the aggregate, for property described in subsection (d)(2)(B), $10,000. .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after December 31, 2025.\n#### 3. Investment tax credit for biomass heating property\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Open-loop biomass heating property credit (a) In general For purposes of section 46, the open-loop biomass heating property credit for any taxable year is 30 percent of the basis of the open-loop biomass heating property placed in service during such taxable year. (b) Open-Loop biomass heating property For purposes of this section\u2014 (1) In general The term open-loop biomass heating property means any property which\u2014 (A) uses open-loop biomass (as defined in section 45(c)(3)) to produce thermal energy in the form of heat, hot water, hot air, or steam, and (B) is used for space heating, air conditioning, domestic hot water, industrial process heat, or any combination of the foregoing. (2) Requirements for boilers and furnaces Such term shall not include any boiler or furnace unless such boiler or furnace\u2014 (A) operates at thermal output efficiencies of not less than 75 percent (measured by the lower heating value of the fuel at nominal output), (B) is installed indoors, (C) operates at a scale smaller than 50 MMBtu, and (D) is equipped with an electrostatic precipitator or other similar emissions control technology. (c) Other rules (1) Special rule for property financed by tax-exempt bonds Rules similar to the rule under section 45(b)(3) shall apply for purposes of this section. (2) Certain Progress Expenditure Rules Made Applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of subsection (a). .\n##### (b) Conforming amendments\n**(1)**\nSection 46 of such Code is amended by striking and at the end of paragraph (6), by striking the period at the end of paragraph (7) and inserting , and , and by adding at the end the following new paragraph:\n(8) the open-loop biomass heating property credit. .\n**(2)**\nSection 49(a)(1)(C) of such Code is amended by striking and at the end of clause (vii), by striking the period at the end of clause (viii), and by adding at the end the follow new clause:\n(ix) the basis of any open-loop biomass heating property credit. .\n**(3)**\nSection 50(a)(2)(E) of such Code is amended by striking or 48E(e) and inserting 48E(e), or 48F(c)(2) .\n**(4)**\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of subtitle A of such Code is amended by adding at the end the following new item:\nSec. 48F. Open-loop biomass heating property credit. .\n##### (c) Effective date\nThe amendments made by this section shall apply to periods after December 31, 2025, in taxable years ending after such date, under rules similar to the rules of section 48(m) of the Internal Revenue Code of 1986 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990).",
      "versionDate": "2025-04-08",
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
        "updateDate": "2025-05-09T17:44:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-08",
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
          "measure-id": "id119s1345",
          "measure-number": "1345",
          "measure-type": "s",
          "orig-publish-date": "2025-04-08",
          "originChamber": "SENATE",
          "update-date": "2026-01-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1345v00",
            "update-date": "2026-01-30"
          },
          "action-date": "2025-04-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>America's First Fuels Act</strong></p><p>This bill increases the federal energy efficient home improvement tax credit amount allowed for installing a biomass stove or biomass boiler in a principal residence. The bill also establishes a new federal tax credit (as part of the general business tax credit) for investments in open-loop biomass heating property.</p><p>Specifically, the bill increases to $10,000 the annual maximum amount of the energy efficient home improvement tax credit allowed for installing a biomass stove or biomass boiler in a principal residence. (Under current law, taxpayers may claim a tax credit of 30% of the cost, up to an annual maximum of $2,000, to install a biomass stove, a biomass boiler, or certain other energy-efficient property in a principal residence.)</p><p>The bill also establishes a new business tax credit for 30% of the cost of any property which (1) uses open-loop biomass to produce thermal energy in the form of heat, hot water, hot air, or steam; and (2) is used for space heating, air conditioning, domestic hot water, or industrial process heat (or any combination of such uses). (Conditions apply.)</p><p>However, the tax credit is reduced for open-loop biomass heating property financed with tax-exempt bonds.</p><p>Finally, under the bill, businesses may elect to claim the tax credit for qualified open-loop biomass heating property progress expenses (expenses incurred in advance of placing such property in service) if the normal construction period for such property is two years or more and certain other conditions are met. \u00a0</p>"
        },
        "title": "America's First Fuels Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1345.xml",
    "summary": {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>America's First Fuels Act</strong></p><p>This bill increases the federal energy efficient home improvement tax credit amount allowed for installing a biomass stove or biomass boiler in a principal residence. The bill also establishes a new federal tax credit (as part of the general business tax credit) for investments in open-loop biomass heating property.</p><p>Specifically, the bill increases to $10,000 the annual maximum amount of the energy efficient home improvement tax credit allowed for installing a biomass stove or biomass boiler in a principal residence. (Under current law, taxpayers may claim a tax credit of 30% of the cost, up to an annual maximum of $2,000, to install a biomass stove, a biomass boiler, or certain other energy-efficient property in a principal residence.)</p><p>The bill also establishes a new business tax credit for 30% of the cost of any property which (1) uses open-loop biomass to produce thermal energy in the form of heat, hot water, hot air, or steam; and (2) is used for space heating, air conditioning, domestic hot water, or industrial process heat (or any combination of such uses). (Conditions apply.)</p><p>However, the tax credit is reduced for open-loop biomass heating property financed with tax-exempt bonds.</p><p>Finally, under the bill, businesses may elect to claim the tax credit for qualified open-loop biomass heating property progress expenses (expenses incurred in advance of placing such property in service) if the normal construction period for such property is two years or more and certain other conditions are met. \u00a0</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119s1345"
    },
    "title": "America's First Fuels Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>America's First Fuels Act</strong></p><p>This bill increases the federal energy efficient home improvement tax credit amount allowed for installing a biomass stove or biomass boiler in a principal residence. The bill also establishes a new federal tax credit (as part of the general business tax credit) for investments in open-loop biomass heating property.</p><p>Specifically, the bill increases to $10,000 the annual maximum amount of the energy efficient home improvement tax credit allowed for installing a biomass stove or biomass boiler in a principal residence. (Under current law, taxpayers may claim a tax credit of 30% of the cost, up to an annual maximum of $2,000, to install a biomass stove, a biomass boiler, or certain other energy-efficient property in a principal residence.)</p><p>The bill also establishes a new business tax credit for 30% of the cost of any property which (1) uses open-loop biomass to produce thermal energy in the form of heat, hot water, hot air, or steam; and (2) is used for space heating, air conditioning, domestic hot water, or industrial process heat (or any combination of such uses). (Conditions apply.)</p><p>However, the tax credit is reduced for open-loop biomass heating property financed with tax-exempt bonds.</p><p>Finally, under the bill, businesses may elect to claim the tax credit for qualified open-loop biomass heating property progress expenses (expenses incurred in advance of placing such property in service) if the normal construction period for such property is two years or more and certain other conditions are met. \u00a0</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119s1345"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1345is.xml"
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
      "title": "America's First Fuels Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "America's First Fuels Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the limitation on the credit for biomass stoves and boilers and to include biomass heating appliances in the energy credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:22Z"
    }
  ]
}
```
