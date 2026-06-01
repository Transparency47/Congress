# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2545?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2545
- Title: Financing Our Energy Future Act
- Congress: 119
- Bill type: HR
- Bill number: 2545
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2025-12-05T21:42:08Z
- Update date including text: 2025-12-05T21:42:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2545",
    "number": "2545",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "E000298",
        "district": "4",
        "firstName": "Ron",
        "fullName": "Rep. Estes, Ron [R-KS-4]",
        "lastName": "Estes",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Financing Our Energy Future Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:42:08Z",
    "updateDateIncludingText": "2025-12-05T21:42:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:07:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2545ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2545\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Estes (for himself and Mr. Thompson of California ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the publicly traded partnership ownership structure to energy power generation projects and transportation fuels, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Financing Our Energy Future Act .\n#### 2. Green energy publicly traded partnerships\n##### (a) In general\nSection 7704(d)(1)(E) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking income and gains derived from the exploration and inserting\nincome and gains derived from\u2014 (i) the exploration ,\n**(2)**\nby inserting or before industrial source , and\n**(3)**\nby striking , or the transportation or storage and all that follows and inserting the following:\n(ii) the generation of electric power or thermal energy exclusively using any qualified energy resource (as defined in section 45(c)(1)), (iii) the operation of energy property (as defined in section 48(a)(3), determined without regard to any date by which the construction of the facility is required to begin), (iv) in the case of a facility described in paragraph (3) or (7) of section 45(d) (determined without regard to any placed in service date or date by which construction of the facility is required to begin), the accepting or processing of open-loop biomass or municipal solid waste, (v) the storage of electric power or thermal energy exclusively using energy storage technology (as defined in section 48(c)(6)), (vi) the generation, storage, or distribution of electric power or thermal energy exclusively using energy property that is combined heat and power system property (as defined in section 48(c)(3), determined without regard to subparagraph (B)(iii) thereof and without regard to any date by which the construction of the facility is required to begin), (vii) the transportation or storage of\u2014 (I) any fuel described in subsection (b), (c), (d), (e), or (k) of section 6426, or (II) liquified hydrogen or compressed hydrogen, (viii) the conversion of renewable biomass (as defined in subparagraph (I) of section 211(o)(1) of the Clean Air Act (as in effect on the date of the enactment of this clause)) into renewable fuel (as defined in subparagraph (J) of such section as so in effect), or the storage or transportation of such fuel, (ix) the production, storage, or transportation of any fuel which\u2014 (I) uses as its primary feedstock carbon oxides captured from an anthropogenic source or the atmosphere, (II) does not use as its primary feedstock carbon oxide which is deliberately released from naturally occurring subsurface springs, and (III) is determined by the Secretary, after consultation with the Secretary of Energy and the Administrator of the Environmental Protection Agency, to achieve a reduction of not less than a 60 percent in lifecycle greenhouse gas emissions (as defined in section 211(o)(1)(H) of the Clean Air Act, as in effect on the date of the enactment of this clause) compared to baseline lifecycle greenhouse gas emissions (as defined in section 211(o)(1)(C) of such Act, as so in effect), (x) the generation of electric power from a qualifying gasification project (as defined in section 48B(c)(1) without regard to subparagraph (C)) that is described in section 48B(d)(1)(B), (xi) in the case of a qualified facility (as defined in section 45Q(d), without regard to any date by which construction of the facility is required to begin) not less than 50 percent of the total carbon oxide production of which is qualified carbon oxide (as defined in section 45Q(c))\u2014 (I) the generation, availability for such generation, or storage of electric power at such facility, or (II) the capture of carbon dioxide by such facility, (xii) the generation of electric power or energy from any advanced nuclear facility (as defined in section 45J(d)(2)), or (xiii) the production, storage, or transportation of any renewable chemical which\u2014 (I) is produced in the United States (or in a territory or possession of the United States) from renewable biomass, (II) is not less than 95 percent biobased content, (III) is not sold or used for the production of any food, feed, fuel, or pharmaceuticals, (IV) is approved to use the USDA Certified Biobased Product label under section 9002(b) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8102(b) ), and (V) is a chemical intermediate (as such term is defined in section 3201.109 of title 7, Code of Federal Regulations (or successor regulations)), .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-02-11",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "510",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Financing Our Energy Future Act",
      "type": "S"
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
        "updateDate": "2025-05-09T13:59:16Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2545ih.xml"
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
      "title": "Financing Our Energy Future Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T06:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Financing Our Energy Future Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T06:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to extend the publicly traded partnership ownership structure to energy power generation projects and transportation fuels, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T06:33:31Z"
    }
  ]
}
```
