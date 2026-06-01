# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3937?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3937
- Title: Homes for American Families Act
- Congress: 119
- Bill type: S
- Bill number: 3937
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-03-19T14:49:31Z
- Update date including text: 2026-03-19T14:49:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3937",
    "number": "3937",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Homes for American Families Act",
    "type": "S",
    "updateDate": "2026-03-19T14:49:31Z",
    "updateDateIncludingText": "2026-03-19T14:49:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
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
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T18:24:53Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3937is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3937\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Mr. Hawley (for himself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Sherman Act to prohibit certain entities from purchasing residential real estate, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Homes for American Families Act .\n#### 2. Amendment\n##### (a) In general\nThe Sherman Act ( 15 U.S.C. 1 et seq. ) is amended by adding at the end the following:\n9. Residential real estate contracts in restraint of trade (a) Definitions In this section: (1) Covered entity (A) In general The term covered entity means\u2014 (i) real estate investment trust; (ii) an insurance company; or (iii) an investment company or private fund\u2014 (I) with assets under management of not less than $150,000,000; or (II) that is directly or indirectly owned or controlled by a person that directly or indirectly owns or controls 1 or more investment companies or private funds with total assets under management of not less than $150,000,000. (B) Aggregation rules For purposes of determining the assets under management of an entity under subparagraph (A)(iii), all persons which are treated as a single employer under subsection (b) or (c) of section 414 of the Internal Revenue Code of 1986 shall be treated as one entity. For purposes of this subsection, in applying section 414(b) of such Code, section 1563 of such Code shall be applied without regard to subsection (b)(2) thereof. (2) Insurance company The term insurance company has the meaning given the term in section 2(a) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20132(a) ). (3) Investment company The term investment company has the meaning given the term in section 3 of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133 ). (4) Private fund The term private fund means a corporation that would be considered an investment company under section 3 of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133 ) but for the application of paragraph (1) or (7) of subsection (c) of such section 3. (5) Real estate investment trust The term real estate investment trust has the meaning given the term in section 856 of the Internal Revenue Code of 1986. (6) Residential real estate The term residential real estate means\u2014 (A) a single-family home; (B) a condominium; (C) a townhouse; and (D) any land that has been zoned by a local government for the development of a property described in subparagraphs (A) through (C). (b) Contracts in restraint of trade (1) In general Except as provided in paragraph (2), any purchase by a covered entity of residential real estate shall be deemed a contract in restraint of trade in violation of section 1, except that the violation shall be civil only and no criminal penalty under that section, including a term of imprisonment, shall apply. (2) Exceptions Paragraph (1) shall not apply to a homebuilder, developer, or redeveloper if the units of residential real estate are being or have been constructed for ownership by a person or entity that is not prohibited from purchasing residential real estate under this subsection. (3) Application Paragraph (1) shall only apply to the purchase of residential real estate on or after the date of enactment of this section. (c) Prioritized antitrust scrutiny and enforcement The Assistant Attorney General in charge of the Antitrust Division of the Department of Justice shall prioritize the review of purchases of residential real estate by a covered entity for anti-competitive effects and prioritize enforcement of antitrust laws, as appropriate, against coordinated vacancy, pricing strategies, and other anticompetitive practices by covered entities in local residential real estate markets. .\n##### (b) Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 90 days after the date of enactment of this Act.",
      "versionDate": "2026-02-26",
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
        "name": "Commerce",
        "updateDate": "2026-03-19T14:49:31Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3937is.xml"
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
      "title": "Homes for American Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Homes for American Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Sherman Act to prohibit certain entities from purchasing residential real estate, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-17T03:48:28Z"
    }
  ]
}
```
