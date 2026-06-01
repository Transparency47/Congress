# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7066?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7066
- Title: SHIELD Act
- Congress: 119
- Bill type: HR
- Bill number: 7066
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-04-03T08:05:39Z
- Update date including text: 2026-04-03T08:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7066",
    "number": "7066",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000593",
        "district": "49",
        "firstName": "Mike",
        "fullName": "Rep. Levin, Mike [D-CA-49]",
        "lastName": "Levin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SHIELD Act",
    "type": "HR",
    "updateDate": "2026-04-03T08:05:39Z",
    "updateDateIncludingText": "2026-04-03T08:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:01:15Z",
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
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "IL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "OH"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "IL"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "ME"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "RI"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-03-30",
      "state": "OH"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7066ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7066\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. Levin (for himself, Ms. Castor of Florida , Mr. Quigley , Mr. Landsman , Mr. Goldman of New York , Mr. Latimer , Mr. Casten , and Ms. Pingree ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to add a standard relating to the consideration of large load facilities as a class of electric consumers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Hikes In Electricity from Large Load Demands Act or the SHIELD Act .\n#### 2. PURPA standards for large load facilities\n##### (a) In general\nSection 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d) ) is amended by adding at the end the following:\n(22) Large load facility class (A) Classification Large load facilities shall be considered a class of electric consumers. (B) Cost recovery relating to large load facility class Each electric utility that provides electric service to a class of electric consumers described in subparagraph (A) shall fully recover from such class all costs associated with any upgrade made to the generation, transmission, or distribution facilities of the electric grid, including local facilities, in order to meet the demand for electric energy from such class, including in the event that a large load facility ceases operations or uses less electric energy than projected at the time of such upgrade. (23) Grid reliability for large load facilities Each electric utility shall prioritize, among requests from owners or operators of large load facilities for electric service, such a request under which the owner or operator agrees to employ\u2014 (A) features that reduce the demand for electric energy from the electric grid during times of peak demand, including\u2014 (i) energy efficiency or energy conservation measures; (ii) onsite energy storage; or (iii) demand response or load flexibility technologies; and (B) zero-emission electric energy generated onsite or procured within the same balancing authority through a power purchase agreement to meet all of the demand of the large load facility for electric energy. .\n##### (b) Definitions\nSection 111 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621 ) is amended by adding at the end the following:\n(e) Definitions For the purposes of subsection (d): (1) Large load facility The term large load facility \u2014 (A) means a facility, or an aggregation of facilities at a single site, with respect to which the peak demand of such facility or such aggregation of facilities exceeds 75 megawatts; and (B) does not include an existing facility with respect to which any increased demand is predominantly caused by electrification or measures to reduce greenhouse gas emissions. (2) Zero-emission electric energy The term zero-emission electric energy means electric energy generated without emitting greenhouse gases, including from solar, wind, geothermal, hydroelectric, tidal, fission, or fusion. .\n##### (c) Conforming amendments\n**(1) Obligations to consider and determine**\nSection 112 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622 ) is amended\u2014\n**(A)**\nin subsection (b), by adding at the end the following:\n(9) (A) Not later than 1 year after the date of enactment of this paragraph, each State regulatory authority (with respect to each electric utility for which the State has ratemaking authority) and each nonregulated utility shall commence consideration under section 111, or set a hearing date for consideration, with respect to each standard established by paragraphs (22) and (23) of section 111(d). (B) Not later than 2 years after the date of enactment of this paragraph, each State regulatory authority (with respect to each electric utility for which the State has ratemaking authority), and each nonregulated electric utility shall complete the consideration and make the determination under section 111 with respect to each standard established by paragraphs (22) and (23) of section 111(d). (C) Not later than 30 days after completing the consideration and making a determination under section 111 with respect to each standard established by paragraphs (22) and (23) of section 111(d), each State regulatory authority (with respect to each electric utility for which the State has ratemaking authority), and each nonregulated electric utility shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Energy and Natural Resources of the Senate a report detailing the process used for consideration and an explanation for the determination. ;\n**(B)**\nin subsection (c)\u2014\n**(i)**\nby striking subsection (b)(2) and inserting subsection (b) ; and\n**(ii)**\nby inserting In the case of the standard established by paragraphs (22) and (23) of section 111(d), the reference contained in this subsection to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of such paragraphs (22) and (23). after paragraph (21). ; and\n**(C)**\nby adding at the end the following:\n(i) Other prior State actions Subsections (b) and (c) shall not apply to the standards established by paragraphs (22) and (23) of section 111(d) in the case of any electric utility in a State if, before the date of enactment of this subsection\u2014 (1) the State has implemented for the electric utility the standard concerned (or a comparable standard); (2) the State regulatory authority for the State or the relevant nonregulated electric utility has conducted a proceeding to consider implementation of the standard concerned (or a comparable standard) for the electric utility; or (3) the State legislature has voted on the implementation of the standard concerned (or a comparable standard) for the electric utility during the 3-year period ending on that date of enactment. .\n**(2) Prior and pending proceedings**\nSection 124 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2634 ) is amended by inserting In the case of each standard established by paragraphs (22) and (23) of section 111(d), the reference contained in this section to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of such paragraphs (22) and (23). after paragraph (21). .",
      "versionDate": "2026-01-14",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-02-04T18:54:12Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7066ih.xml"
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
      "title": "SHIELD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHIELD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Hikes In Electricity from Large Load Demands Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to add a standard relating to the consideration of large load facilities as a class of electric consumers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:59Z"
    }
  ]
}
```
