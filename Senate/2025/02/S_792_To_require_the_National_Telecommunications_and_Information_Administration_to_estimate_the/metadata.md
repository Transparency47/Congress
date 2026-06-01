# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/792?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/792
- Title: Government Spectrum Valuation Act
- Congress: 119
- Bill type: S
- Bill number: 792
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-03-26T12:20:41Z
- Update date including text: 2025-03-26T12:20:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/792",
    "number": "792",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Government Spectrum Valuation Act",
    "type": "S",
    "updateDate": "2025-03-26T12:20:41Z",
    "updateDateIncludingText": "2025-03-26T12:20:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T18:38:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s792is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 792\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the National Telecommunications and Information Administration to estimate the value of electromagnetic spectrum assigned or otherwise allocated to Federal entities.\n#### 1. Short title\nThis Act may be cited as the Government Spectrum Valuation Act .\n#### 2. Estimate of value of electromagnetic spectrum\n##### (a) In general\nPart A of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 901 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 105 ( 47 U.S.C. 904 ) as section 106; and\n**(2)**\nby inserting after section 104 ( 47 U.S.C. 903 ) the following:\n105. Estimate of value of electromagnetic spectrum (a) Definitions In this section\u2014 (1) the term covered band means the band of frequencies between 3 kilohertz and 95 gigahertz; (2) the term Federal entity has the meaning given the term in section 113(l); and (3) the term OMB means the Office of Management and Budget. (b) Estimates required The NTIA, in consultation with the Commission and OMB, shall estimate the value of electromagnetic spectrum in the covered band that is assigned or otherwise allocated to each Federal entity as of the date of the estimate, in accordance with the schedule under subsection (c). (c) Schedule The NTIA shall conduct the estimates under subsection (b) for the frequencies between\u2014 (1) 3 kilohertz and 33 gigahertz not later than 1 year after the date of enactment of this section, and every 3 years thereafter; (2) 33 gigahertz and 66 gigahertz not later than 2 years after the date of enactment of this section, and every 3 years thereafter; and (3) 66 gigahertz and 95 gigahertz not later than 3 years after the date of enactment of this section, and every 3 years thereafter. (d) Basis for estimate (1) In general The NTIA shall base each value estimate under subsection (b) on the value that the electromagnetic spectrum would have if the spectrum were reallocated for the use with the highest potential value of licensed or unlicensed commercial wireless services that do not have access to that spectrum as of the date of the estimate. (2) Consideration of Government capabilities In estimating the value of spectrum under subsection (b), the NTIA may consider the spectrum needs of commercial interests while preserving the spectrum access necessary to satisfy mission requirements and operations of Federal entities. (3) Dynamic scoring To the greatest extent practicable, the NTIA shall incorporate dynamic scoring methodology into the value estimate under subsection (b). (4) Disclosure (A) In general Subject to subparagraph (B), the NTIA shall publicly disclose how the NTIA arrived at each value estimate under subsection (b), including any findings made under paragraph (2) of this subsection. (B) Classified, law enforcement-sensitive, and proprietary information If any information involved in a value estimate under subsection (b), including any finding made under paragraph (2) of this subsection, is classified, law enforcement-sensitive, or proprietary, the NTIA\u2014 (i) may not publicly disclose the classified, law enforcement-sensitive, or proprietary information; and (ii) shall make the classified, law enforcement-sensitive, or proprietary information available to any Member of Congress, upon request, in a classified annex. (e) Agency report on value of electromagnetic spectrum A Federal entity that has been assigned or otherwise allocated use of electromagnetic spectrum within the covered band shall report the value of the spectrum as most recently estimated under subsection (b)\u2014 (1) in the budget of the Federal entity to be included in the budget of the United States Government submitted by the President under section 1105 of title 31, United States Code; and (2) in the annual financial statement of the Federal entity required to be filed under section 3515 of title 31, United States Code. .\n##### (b) Technical and conforming amendments\nSection 103(b) of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 902(b) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking section 105(d) and inserting section 106(d) ; and\n**(2)**\nin paragraph (2), in the matter preceding subparagraph (A), by striking section 105(d) and inserting section 106(d) .",
      "versionDate": "2025-02-27",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-10T18:10:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s792",
          "measure-number": "792",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s792v00",
            "update-date": "2025-03-26"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Government Spectrum Valuation Act </strong></p><p>This bill requires the National Telecommunications and Information Administration (NTIA) to periodically estimate the value of specified electromagnetic spectrum that is allocated to federal agencies.</p><p>Each federal agency that is assigned or allocated a portion of that spectrum must include the most recent estimated value of its spectrum, as determined by NTIA,\u00a0in its annual budget and financial statements.</p>"
        },
        "title": "Government Spectrum Valuation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s792.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Government Spectrum Valuation Act </strong></p><p>This bill requires the National Telecommunications and Information Administration (NTIA) to periodically estimate the value of specified electromagnetic spectrum that is allocated to federal agencies.</p><p>Each federal agency that is assigned or allocated a portion of that spectrum must include the most recent estimated value of its spectrum, as determined by NTIA,\u00a0in its annual budget and financial statements.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119s792"
    },
    "title": "Government Spectrum Valuation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Government Spectrum Valuation Act </strong></p><p>This bill requires the National Telecommunications and Information Administration (NTIA) to periodically estimate the value of specified electromagnetic spectrum that is allocated to federal agencies.</p><p>Each federal agency that is assigned or allocated a portion of that spectrum must include the most recent estimated value of its spectrum, as determined by NTIA,\u00a0in its annual budget and financial statements.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119s792"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s792is.xml"
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
      "title": "Government Spectrum Valuation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T16:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Government Spectrum Valuation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T16:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the National Telecommunications Information Administration to estimate the value of electromagnetic spectrum assigned or otherwise allocated to Federal entities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T16:18:22Z"
    }
  ]
}
```
