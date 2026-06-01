# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6116
- Title: Safe Hydration is an American Right in Energy Development Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6116
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-04-10T11:59:48Z
- Update date including text: 2026-04-10T11:59:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6116",
    "number": "6116",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Safe Hydration is an American Right in Energy Development Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T11:59:48Z",
    "updateDateIncludingText": "2026-04-10T11:59:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:00:25Z",
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
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "VA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "FL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NY"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CO"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "WA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "WI"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "TN"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NY"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "IN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MI"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MA"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6116ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6116\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Ms. Schakowsky (for herself, Mr. Beyer , Ms. Castor of Florida , Ms. Clarke of New York , Ms. DeGette , Ms. Jayapal , Mr. Pocan , Mr. Huffman , Mr. Vargas , Mr. Cohen , Mr. Morelle , Mr. DeSaulnier , Mr. Casten , Mr. Carson , Mr. Thanedar , Mr. Khanna , Mr. McGovern , Mr. Espaillat , Mr. Sherman , and Ms. Simon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Safe Drinking Water Act to require testing of underground sources of drinking water in connection with hydraulic fracturing operations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Hydration is an American Right in Energy Development Act of 2025 .\n#### 2. Testing of underground drinking water sources in connection with hydraulic fracturing operations\n##### (a) In general\nSection 1421(b)(1) of the Safe Drinking Water Act ( 42 U.S.C. 300h(b)(1) ) is amended\u2014\n**(1)**\nin subparagraph (C), by striking and at the end;\n**(2)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(E) shall prohibit the underground injection of fluids or propping agents pursuant to hydraulic fracturing operations related to oil, gas, or geothermal production activities unless the person proposing to conduct the hydraulic fracturing operations agrees to conduct testing and report data in accordance with section 1421A. .\n##### (b) Testing and reporting requirements\nPart C of the Safe Drinking Water Act is amended by inserting after section 1421 of such Act ( 42 U.S.C. 300h ) the following:\n1421A. Testing of underground drinking water sources in connection with hydraulic fracturing operations (a) Requirements Regulations under section 1421(a) for State underground injection control programs shall, in connection with the underground injection of fluids or propping agents pursuant to hydraulic fracturing operations related to oil, gas, or geothermal production activities, require any person conducting such operations\u2014 (1) to conduct testing of underground sources of drinking water in accordance with subsections (c) and (d)\u2014 (A) with respect to a site where, as of the date of enactment of this section, underground injection has not commenced for the first time\u2014 (i) prior to commencement of underground injection at the site for the first time; (ii) at least once every 6 months during the period beginning at the commencement of underground injection described in clause (i) and ending at the cessation of such hydraulic fracturing operations; and (iii) at least once every 12 months during the 5-year period following the end of the period described in clause (ii); (B) with respect to a site where, as of the date of enactment of this section, there is no active underground injection, but underground injection has previously occurred at the site\u2014 (i) prior to renewing underground injection at the site; (ii) at least once every 6 months during the period beginning at such renewal of underground injection and ending at the cessation of such hydraulic fracturing operations; and (iii) at least once every 12 months during the 5-year period following the end of the period described in clause (ii); and (C) with respect to a site where, as of the date of enactment of this section, such hydraulic fracturing operations are occurring\u2014 (i) at least once every 6 months during the period beginning on the date of enactment of this section ending at the cessation of such hydraulic fracturing operations; and (ii) at least once every 12 months during the 5-year period following the end of the period described in clause (i); and (2) to submit reports to the Administrator on the results of testing under subparagraph (A), (B), or (C) of paragraph (1) within 2 weeks of such testing. (b) Exception The testing and reporting requirements of subsection (a) do not apply with respect to hydraulic fracturing operations if there is no accessible underground source of drinking water within a radius of one mile of the site where the operations occur. (c) Sampling locations Testing required pursuant to subsection (a) shall occur\u2014 (1) at all accessible underground sources of drinking water within a radius of one-half mile of the site where the hydraulic fracturing operations occur; and (2) if there is no accessible underground source of drinking water within such radius, at the nearest accessible underground source of drinking water within a radius of one mile of such site. (d) Testing Testing required pursuant to subsection (a) shall\u2014 (1) be conducted by one or more laboratories certified pursuant to the Environmental Protection Agency\u2019s program for certifying laboratories for analysis of drinking water contaminants; and (2) include testing for any hazardous substance, pollutant, contaminant, or other factor that the Administrator determines would indicate damage associated with hydraulic fracturing operations. (e) Database; public accessibility (1) Database The Administrator shall establish and maintain a database of the results reported pursuant to subsection (a)(2). (2) Public accessibility The Administrator shall make such database publicly accessible on the website of the Environmental Protection Agency. (3) Public searchability The Administrator shall make such database searchable by ZIP Code, allowing members of the public to easily identify all sites for which reports are submitted pursuant to subsection (a)(2). (f) Definition In this section, the term accessible underground source of drinking water means an underground source of drinking water to which the person conducting the hydraulic fracturing operations can reasonably gain access. .\n##### (c) Conforming amendment\nSection 1421(d)(1)(B)(ii) of the Safe Drinking Water Act ( 42 U.S.C. 300h(d)(1)(B)(ii) ) is amended by inserting except as provided in subsection (b)(1)(E) of this section and section 1421A, before the underground injection of fluids or propping agents (other than diesel fuels) pursuant to hydraulic fracturing operations related to oil, gas, or geothermal production activities .",
      "versionDate": "2025-11-18",
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
        "name": "Environmental Protection",
        "updateDate": "2025-12-04T15:45:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-18",
    "originChamber": "House",
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
          "measure-id": "id119hr6116",
          "measure-number": "6116",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-18",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6116v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2025-11-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Safe Hydration is an American Right in Energy Development Act of 2025</strong></p><p>This bill requires hydraulic fracturing operations to test for and report on\u00a0underground sources of drinking water that are contaminated by\u00a0such operations. Hydraulic fracturing, or fracking, is a process to extract underground resources such as oil or gas from a geologic formation by injecting water, a propping agent (e.g., sand), and chemical additives into a well under enough pressure to fracture the geological formation.</p><p>Specifically, this bill modifies\u00a0requirements governing state underground injection control programs. In order to obtain primary enforcement responsibility for\u00a0such\u00a0programs, states must prohibit the underground injection of fluids or propping agents pursuant to hydraulic fracturing operations related to oil, gas, or geothermal production activities unless the hydraulic fracturing operations agree to test for and report on contamination of drinking water.</p><p>Hydraulic fracturing operations are exempted from those testing and reporting requirements if there is no accessible underground source of drinking water within a radius of one mile of the site where the operations occur.</p><p>The Environmental\u00a0Protection Agency\u00a0must establish and maintain a publicly accessible and searchable database of the testing results.</p>"
        },
        "title": "Safe Hydration is an American Right in Energy Development Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6116.xml",
    "summary": {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe Hydration is an American Right in Energy Development Act of 2025</strong></p><p>This bill requires hydraulic fracturing operations to test for and report on\u00a0underground sources of drinking water that are contaminated by\u00a0such operations. Hydraulic fracturing, or fracking, is a process to extract underground resources such as oil or gas from a geologic formation by injecting water, a propping agent (e.g., sand), and chemical additives into a well under enough pressure to fracture the geological formation.</p><p>Specifically, this bill modifies\u00a0requirements governing state underground injection control programs. In order to obtain primary enforcement responsibility for\u00a0such\u00a0programs, states must prohibit the underground injection of fluids or propping agents pursuant to hydraulic fracturing operations related to oil, gas, or geothermal production activities unless the hydraulic fracturing operations agree to test for and report on contamination of drinking water.</p><p>Hydraulic fracturing operations are exempted from those testing and reporting requirements if there is no accessible underground source of drinking water within a radius of one mile of the site where the operations occur.</p><p>The Environmental\u00a0Protection Agency\u00a0must establish and maintain a publicly accessible and searchable database of the testing results.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6116"
    },
    "title": "Safe Hydration is an American Right in Energy Development Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe Hydration is an American Right in Energy Development Act of 2025</strong></p><p>This bill requires hydraulic fracturing operations to test for and report on\u00a0underground sources of drinking water that are contaminated by\u00a0such operations. Hydraulic fracturing, or fracking, is a process to extract underground resources such as oil or gas from a geologic formation by injecting water, a propping agent (e.g., sand), and chemical additives into a well under enough pressure to fracture the geological formation.</p><p>Specifically, this bill modifies\u00a0requirements governing state underground injection control programs. In order to obtain primary enforcement responsibility for\u00a0such\u00a0programs, states must prohibit the underground injection of fluids or propping agents pursuant to hydraulic fracturing operations related to oil, gas, or geothermal production activities unless the hydraulic fracturing operations agree to test for and report on contamination of drinking water.</p><p>Hydraulic fracturing operations are exempted from those testing and reporting requirements if there is no accessible underground source of drinking water within a radius of one mile of the site where the operations occur.</p><p>The Environmental\u00a0Protection Agency\u00a0must establish and maintain a publicly accessible and searchable database of the testing results.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6116"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6116ih.xml"
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
      "title": "Safe Hydration is an American Right in Energy Development Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T10:08:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Hydration is an American Right in Energy Development Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T10:08:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Safe Drinking Water Act to require testing of underground sources of drinking water in connection with hydraulic fracturing operations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T10:03:29Z"
    }
  ]
}
```
