# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4147?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4147
- Title: Fair Prices for Local Businesses Act
- Congress: 119
- Bill type: S
- Bill number: 4147
- Origin chamber: Senate
- Introduced date: 2026-03-19
- Update date: 2026-04-17T19:42:02Z
- Update date including text: 2026-04-17T19:42:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in Senate
- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-19: Introduced in Senate

## Actions

- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4147",
    "number": "4147",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Fair Prices for Local Businesses Act",
    "type": "S",
    "updateDate": "2026-04-17T19:42:02Z",
    "updateDateIncludingText": "2026-04-17T19:42:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T18:48:30Z",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "VT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "AZ"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "PA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4147is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4147\nIN THE SENATE OF THE UNITED STATES\nMarch 19, 2026 Mr. Murphy (for himself, Mr. Welch , Mr. Gallego , Mr. Fetterman , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo strengthen the prohibition on price discrimination under the Clayton Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Prices for Local Businesses Act .\n#### 2. Clayton Act amendments\n##### (a) In general\nThe Clayton Act ( 15 U.S.C. 12 et seq. ) is amended\u2014\n**(1)**\nin section 2 ( 15 U.S.C. 13 )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking in commerce each place it appears and inserting in commerce or in any activity affecting commerce ;\n**(ii)**\nby striking commodities each place it appears and inserting products or services ;\n**(iii)**\nby inserting service provision, after sale, ;\n**(iv)**\nby striking goods, wares, or merchandise and inserting products or services ;\n**(v)**\nby striking goods each place it appears and inserting products or services ; and\n**(vi)**\nby inserting functional discounts or after due allowance for ;\n**(B)**\nin subsection (b)\u2014\n**(i)**\nby inserting including a person charged with inducing or receiving such discrimination, after person charged with a violation of this section, ; and\n**(ii)**\nby striking : Provided, however, That nothing herein contained shall prevent a seller rebutting the prima-facie case thus made by showing that his lower price or the furnishing of services or facilities to any purchaser or purchasers was made in good faith to meet an equally low price of a competitor, or the services or facilities furnished by a competitor ;\n**(C)**\nin subsection (c)\u2014\n**(i)**\nby striking in commerce and inserting in commerce or in any activity affecting commerce ; and\n**(ii)**\nby striking goods, wares, or merchandise and inserting products or services ;\n**(D)**\nin subsection (d)\u2014\n**(i)**\nby striking in commerce and inserting in commerce or in any activity affecting commerce ; and\n**(ii)**\nby striking products or commodities each place it appears and inserting products or services ;\n**(E)**\nin subsection (e)\u2014\n**(i)**\nby inserting engaged in commerce or in any activity affecting commerce after any person ; and\n**(ii)**\nby striking commodity each place it appears and inserting product or service ;\n**(F)**\nby amending subsection (f) to read as follows:\n(f) (1) Subject to paragraph (2), it shall be unlawful for any person engaged in commerce or in any activity affecting commerce, in the course of such commerce or in the course of any activity affecting commerce, to induce or receive the benefit of any violation of this section. (2) In the case of a person with annual retail sales that do not exceed $100,000,000,000, paragraph (1) shall only apply if the person knowingly induced or received the benefit of the violation of this section. ; and\n**(G)**\nby adding at the end the following:\n(g) For purposes of this section\u2014 (1) the term purchase means to pay or grant anything of value in exchange for a product or service; and (2) the term purchaser means a person who pays or grants anything of value in exchange for a product or service, whether or not\u2014 (A) title passes to the payor or grantor; and (B) the payor or grantor exercises dominion or control over the product or service. ; and\n**(2)**\nin section 4 ( 15 U.S.C. 15 )\u2014\n**(A)**\nin subsection (a), by inserting and (c) after Except as provided in subsection (b) ;\n**(B)**\nby redesignating subsection (c) as subsection (d); and\n**(C)**\nby inserting after subsection (b) the following:\n(c) In an action brought with respect to a violation of any subsection of section 2, the plaintiff, upon a showing of proof that the plaintiff has been unlawfully discriminated against by the defendant\u2014 (1) shall conclusively be presumed to have sustained injury and damages equal to the monetary amount or equivalent of the unlawful discrimination; and (2) may establish damages in addition to the damages described in paragraph (1), if any, that the plaintiff sustained as a result of the discrimination. .\n##### (b) Applicability\nThe amendments made by this Act shall apply to transactions occurring on or after the date of enactment of this Act.",
      "versionDate": "2026-03-19",
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
        "actionDate": "2026-04-02",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "8184",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fair Prices for Local Businesses Act",
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
        "name": "Commerce",
        "updateDate": "2026-04-02T19:05:01Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4147is.xml"
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
      "title": "Fair Prices for Local Businesses Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Prices for Local Businesses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to strengthen the prohibition on price discrimination under the Clayton Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T05:18:34Z"
    }
  ]
}
```
