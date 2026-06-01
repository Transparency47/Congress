# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3143?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3143
- Title: State Planning for Reliability and Affordability Act
- Congress: 119
- Bill type: HR
- Bill number: 3143
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2025-12-05T21:58:31Z
- Update date including text: 2025-12-05T21:58:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3143",
    "number": "3143",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "State Planning for Reliability and Affordability Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:58:31Z",
    "updateDateIncludingText": "2025-12-05T21:58:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-05-01T13:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3143ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3143\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Evans of Colorado (for himself and Mr. Langworthy ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to add a standard related to State consideration of reliable generation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the State Planning for Reliability and Affordability Act .\n#### 2. State consideration of reliable generation\n##### (a) In general\nSection 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d) ) is amended by adding at the end the following:\n(22) Ensuring electric reliability with reliable generation facilities (A) In general Each electric utility that employs integrated resource planning shall establish, as part of such integrated resource planning, measures, sufficient to ensure the reliable availability of electric energy over a 10-year period, to maintain\u2014 (i) the operation of reliable generation facilities; or (ii) the procurement of electric energy from reliable generation facilities. (B) Reliable generation facility defined In this paragraph, the term reliable generation facility means an electric generation facility that ensures the reliable availability of electric energy by\u2014 (i) having operational characteristics to enable the generation of electric energy on a continuous basis for a period of not fewer than 30 days; (ii) having\u2014 (I) adequate fuel, or a continuously available energy source, on-site to enable the generation of electric energy on a continuous basis for a period of not fewer than 30 days; or (II) contractual obligations that ensure adequate fuel supply to achieve the generation of electric energy on a continuous basis for a period of not fewer than 30 days; (iii) having operational characteristics to enable the generation of electric energy during emergency and severe weather conditions; and (iv) providing essential services related to the reliable availability of electric energy, including frequency support and voltage support. .\n##### (b) Conforming amendments\n**(1) Obligations to consider and determine**\nSection 112 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622 ) is amended\u2014\n**(A)**\nin subsection (b), by adding at the end the following:\n(9) (A) Not later than 1 year after the date of enactment of this paragraph, each State regulatory authority (with respect to each electric utility for which the State has ratemaking authority) and each nonregulated utility shall commence consideration under section 111, or set a hearing date for consideration, with respect to the standard established by paragraph (22) of section 111(d). (B) Not later than 2 years after the date of enactment of this paragraph, each State regulatory authority (with respect to each electric utility for which the State has ratemaking authority), and each nonregulated electric utility shall complete the consideration and make the determination under section 111 with respect to the standard established by paragraph (22) of section 111(d). ;\n**(B)**\nin subsection (c)\u2014\n**(i)**\nby striking subsection (b)(2) and inserting subsection (b) ; and\n**(ii)**\nby inserting In the case of the standard established by paragraph (22) of section 111(d), the reference contained in this subsection to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of that paragraph (22). after paragraph (21). ; and\n**(C)**\nby adding at the end the following:\n(i) Other prior State actions Subsections (b) and (c) shall not apply to the standard established by paragraph (22) of section 111(d) in the case of any electric utility in a State if, before the date of enactment of this subsection\u2014 (1) the State has implemented for the electric utility the standard (or a comparable standard); (2) the State regulatory authority for the State or the relevant nonregulated electric utility has conducted a proceeding to consider implementation of the standard (or a comparable standard) for the electric utility; or (3) the State legislature has voted on the implementation of the standard (or a comparable standard) for the electric utility during the 3-year period ending on that date of enactment. .\n**(2) Prior and pending proceedings**\nSection 124 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2634 ) is amended by inserting In the case of the standard established by paragraph (22) of section 111(d), the reference contained in this section to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of that paragraph (22). after paragraph (21). .",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-09-19",
        "text": "Placed on the Union Calendar, Calendar No. 260."
      },
      "number": "3628",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "State Planning for Reliability and Affordability Act",
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
        "name": "Energy",
        "updateDate": "2025-05-21T13:21:23Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3143ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "State Planning for Reliability and Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "State Planning for Reliability and Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to add a standard related to State consideration of reliable generation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:16Z"
    }
  ]
}
```
