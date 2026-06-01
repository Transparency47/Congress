# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/120?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/120
- Title: Disaster Housing Reform for American Families Act
- Congress: 119
- Bill type: S
- Bill number: 120
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-03-11T11:03:19Z
- Update date including text: 2026-03-11T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/120",
    "number": "120",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Disaster Housing Reform for American Families Act",
    "type": "S",
    "updateDate": "2026-03-11T11:03:19Z",
    "updateDateIncludingText": "2026-03-11T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
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
            "date": "2025-01-16T18:38:17Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-16T18:38:17Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s120is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 120\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Cassidy (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to establish a pilot program for the construction of temporary disaster assistance housing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Housing Reform for American Families Act .\n#### 2. Disaster assistance housing pilot program\nSection 408(c) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174(c) ) is amended by adding at the end the following:\n(5) Pilot program (A) Definitions In this paragraph: (i) Distributor; manufactured home; manufacturer; retailer The terms distributor , manufactured home , manufacturer , and retailer have the meanings given those terms in section 603 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402 ). (ii) Eligible entity The term eligible entity means\u2014 (I) a manufacturer, distributor, or retailer of a manufactured home or a modular home; and (II) a producer of modular housing. (iii) Secretary The term Secretary means the Secretary of Housing and Urban Development, in coordination with the Administrator of the Federal Emergency Management Agency. (B) Establishment The President shall establish a pilot program under which the President enters into a contract with an eligible entity for the purpose of constructing temporary housing to serve as a type of housing available to individuals and households under subsection (b)(1). (C) Requirements Housing constructed pursuant to subparagraph (B) shall\u2014 (i) be in the form of a manufactured or modular housing structure with not more than 4 units; (ii) be available to individuals and households not later than 90 days (or 120 days, upon extension by the Secretary) after the date on which the President declares a major disaster; (iii) subject to subparagraph (D)(ii), conform with, as applicable\u2014 (I) construction standards of the National Flood Insurance Program; (II) standards for new construction under the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5401 et seq. ); (III) standards under the most recent or second most recent edition of the International Residential Code; (IV) applicable building codes in the State, local, or Tribal jurisdiction in which the housing is located; (V) requirements of the Federal Flood Risk Management Standard of the Federal Emergency Management Agency; (VI) local zoning ordinances; (VII) the national technical standard for flood resistant design and construction (ASCE/SEI 24\u201314); or (VIII) the manufactured home and construction safety standards under part 3280 of title 24, Code of Regulations, or any successor regulation; (iv) reflect the needs of the community in which the housing is constructed according to the type of major disaster experienced by the community; and (v) provide a minimum level of protection against natural hazards for the purpose of protecting the health, safety, and general welfare of the users of the housing against disasters. (D) Permanence; waiver Housing constructed pursuant to subparagraph (B) may\u2014 (i) have the capacity to become permanent housing after the date on which a major disaster declaration terminates; and (ii) receive a waiver for a requirement described in subparagraph (C)(iii) from the Secretary. (E) Transfer guidelines The President, in coordination with the Secretary, shall establish guidelines for the transfer of housing constructed under subparagraph (B) to an established affordable housing program administered by a locality, public housing authority, nonprofit organization, or affordable housing developer after the date on which the disaster declaration for the major disaster for which the housing is constructed terminates. (F) Termination The program established pursuant to subparagraph (B) shall terminate on the date that is 5 years after the date of enactment of the Disaster Housing Reform for American Families Act . (6) Closing costs The President may provide financial assistance to individuals or households affected by a major disaster and purchasing a residential property for closing costs associated with obtaining a mortgage from a Federal program that provides affordable financing options. .",
      "versionDate": "2025-01-16",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-01T20:44:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s120",
          "measure-number": "120",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s120v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Disaster Housing Reform for American Families Act</strong></p><p>This bill requires the Federal Emergency Management Agency (FEMA) to establish a five-year pilot program under the Individuals and Households Program (IHP) through which FEMA contracts to provide factory-built housing to serve disaster survivors until the disaster declaration terminates and then be utilized for affordable housing. It also authorizes\u00a0FEMA to provide IHP grants for closing costs associated with obtaining certain mortgages.\u00a0</p><p>Specifically,\u00a0FEMA must enter into a contract with a producer or seller of manufactured or modular homes to construct such housing\u00a0as a type of temporary housing assistance under IHP. The bill requires the housing to meet specified criteria, including that it must be available within 90 days (unless extended to 120 days) after the disaster declaration, have no more than four units, and provide a minimum level of protection from natural hazards. The housing must conform to various specified standards, but the bill authorizes the Department of Housing and Urban Development to waive any such requirement for construction under the pilot program.</p><p>Also, the bill requires\u00a0FEMA to establish guidelines for transferring the housing to an affordable housing program after the termination of the relevant disaster declaration. However, the bill also authorizes it to become permanent housing after the declaration terminates.</p><p>In addition, the bill authorizes\u00a0FEMA to provide IHP grants to disaster-impacted individuals or households purchasing residential property for closing costs associated with obtaining a mortgage from a federal program providing affordable financing options.</p>"
        },
        "title": "Disaster Housing Reform for American Families Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s120.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disaster Housing Reform for American Families Act</strong></p><p>This bill requires the Federal Emergency Management Agency (FEMA) to establish a five-year pilot program under the Individuals and Households Program (IHP) through which FEMA contracts to provide factory-built housing to serve disaster survivors until the disaster declaration terminates and then be utilized for affordable housing. It also authorizes\u00a0FEMA to provide IHP grants for closing costs associated with obtaining certain mortgages.\u00a0</p><p>Specifically,\u00a0FEMA must enter into a contract with a producer or seller of manufactured or modular homes to construct such housing\u00a0as a type of temporary housing assistance under IHP. The bill requires the housing to meet specified criteria, including that it must be available within 90 days (unless extended to 120 days) after the disaster declaration, have no more than four units, and provide a minimum level of protection from natural hazards. The housing must conform to various specified standards, but the bill authorizes the Department of Housing and Urban Development to waive any such requirement for construction under the pilot program.</p><p>Also, the bill requires\u00a0FEMA to establish guidelines for transferring the housing to an affordable housing program after the termination of the relevant disaster declaration. However, the bill also authorizes it to become permanent housing after the declaration terminates.</p><p>In addition, the bill authorizes\u00a0FEMA to provide IHP grants to disaster-impacted individuals or households purchasing residential property for closing costs associated with obtaining a mortgage from a federal program providing affordable financing options.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s120"
    },
    "title": "Disaster Housing Reform for American Families Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disaster Housing Reform for American Families Act</strong></p><p>This bill requires the Federal Emergency Management Agency (FEMA) to establish a five-year pilot program under the Individuals and Households Program (IHP) through which FEMA contracts to provide factory-built housing to serve disaster survivors until the disaster declaration terminates and then be utilized for affordable housing. It also authorizes\u00a0FEMA to provide IHP grants for closing costs associated with obtaining certain mortgages.\u00a0</p><p>Specifically,\u00a0FEMA must enter into a contract with a producer or seller of manufactured or modular homes to construct such housing\u00a0as a type of temporary housing assistance under IHP. The bill requires the housing to meet specified criteria, including that it must be available within 90 days (unless extended to 120 days) after the disaster declaration, have no more than four units, and provide a minimum level of protection from natural hazards. The housing must conform to various specified standards, but the bill authorizes the Department of Housing and Urban Development to waive any such requirement for construction under the pilot program.</p><p>Also, the bill requires\u00a0FEMA to establish guidelines for transferring the housing to an affordable housing program after the termination of the relevant disaster declaration. However, the bill also authorizes it to become permanent housing after the declaration terminates.</p><p>In addition, the bill authorizes\u00a0FEMA to provide IHP grants to disaster-impacted individuals or households purchasing residential property for closing costs associated with obtaining a mortgage from a federal program providing affordable financing options.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s120"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s120is.xml"
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
      "title": "Disaster Housing Reform for American Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disaster Housing Reform for American Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to establish a pilot program for the construction of temporary disaster assistance housing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:21Z"
    }
  ]
}
```
