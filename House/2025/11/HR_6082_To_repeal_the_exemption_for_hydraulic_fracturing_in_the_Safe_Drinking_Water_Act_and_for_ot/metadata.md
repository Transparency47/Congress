# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6082?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6082
- Title: Fracturing Responsibility and Awareness of Chemicals Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6082
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-04-10T11:19:27Z
- Update date including text: 2026-04-10T11:19:27Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6082",
    "number": "6082",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "D000197",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. DeGette, Diana [D-CO-1]",
        "lastName": "DeGette",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Fracturing Responsibility and Awareness of Chemicals Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T11:19:27Z",
    "updateDateIncludingText": "2026-04-10T11:19:27Z"
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
          "date": "2025-11-18T15:00:05Z",
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
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MI"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "WA"
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "DC"
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
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NY"
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6082ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6082\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Ms. DeGette (for herself, Mr. Beyer , Ms. Castor of Florida , Ms. Clarke of New York , Mr. Huffman , Ms. Jayapal , Mr. Pocan , Ms. Schakowsky , Ms. Tlaib , Mr. Smith of Washington , Mr. Vargas , Ms. Norton , Mr. Khanna , Ms. Meng , Mr. Cohen , Mr. Thanedar , Mr. Morelle , Mr. DeSaulnier , Mr. Casten , Mr. Carson , Mr. McGovern , Mr. Sherman , and Ms. Simon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo repeal the exemption for hydraulic fracturing in the Safe Drinking Water Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fracturing Responsibility and Awareness of Chemicals Act of 2025 .\n#### 2. Regulation of hydraulic fracturing\n##### (a) Hydraulic Fracturing\nSection 1421(d)(1) of the Safe Drinking Water Act ( 42 U.S.C. 300h(d)(1) ) is amended by striking subparagraph (B) and inserting the following:\n(B) includes the underground injection of fluids or propping agents pursuant to hydraulic fracturing operations related to oil, gas, or geothermal production activities; but (C) excludes the underground injection of natural gas for purposes of storage. .\n##### (b) Disclosure of hydraulic fracturing chemicals; medical emergencies; proprietary chemical formulas\nSection 1421(b) of the Safe Drinking Water Act ( 42 U.S.C. 300h(b) ) is amended by adding at the end the following:\n(4) (A) Regulations included under paragraph (1)(C) shall include the following requirements: (i) A person conducting hydraulic fracturing operations shall disclose to the State (or the Administrator if the Administrator has primary enforcement responsibility in the State)\u2014 (I) prior to the commencement of any hydraulic fracturing operations at any lease area or portion thereof, a list of chemicals intended for use in any underground injection during such operations, including identification of the chemical constituents of mixtures, Chemical Abstracts Service numbers for each chemical and constituent, material safety data sheets when available, and the anticipated volume of each chemical; and (II) not later than 30 days after the end of any hydraulic fracturing operations, the list of chemicals used in each underground injection during such operations, including identification of the chemical constituents of mixtures, Chemical Abstracts Service numbers for each chemical and constituent, material safety data sheets when available, and the volume of each chemical used. (ii) The State or the Administrator, as applicable, shall make the disclosure of chemical constituents referred to in clause (i) available to the public, including by posting the information on an appropriate internet website. (iii) Whenever the State or the Administrator, or a treating physician or nurse, determines that a medical emergency exists and the proprietary chemical formula of a chemical used in hydraulic fracturing operations is necessary for medical treatment, the person conducting the hydraulic fracturing operations shall, upon request, immediately disclose the proprietary chemical formulas or the specific chemical identity of a trade secret chemical to the State, the Administrator, or the treating physician or nurse, regardless of whether a written statement of need or a confidentiality agreement has been provided. The person conducting the hydraulic fracturing operations may require a written statement of need and a confidentiality agreement as soon thereafter as circumstances permit. (B) Subparagraph (A)(i) and (A)(ii) do not authorize the State (or the Administrator) to require the public disclosure of proprietary chemical formulas. .",
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
        "updateDate": "2025-12-01T19:44:17Z"
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
          "measure-id": "id119hr6082",
          "measure-number": "6082",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-18",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6082v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2025-11-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fracturing Responsibility and Awareness of Chemicals Act of 2025</strong></p><p>This bill modifies drinking water requirements concerning hydraulic fracturing (fracking) operations, including by giving the Environmental Protection Agency (EPA) the authority to protect groundwater sources (e.g., wells) from certain pollution risks posed by fracking operations.</p><p>The bill also establishes requirements for disclosing the chemicals intended for use in fracking operations as well as the chemicals actually used in the operations. If the proprietary chemical formulas of chemicals used in fracking operations are necessary for treatment in medical emergencies, then the operations must disclose the formulas or the specific chemical identities of trade secret chemicals to the state, the EPA, or the treating physicians or nurses upon request, regardless of whether written statements of need or confidentiality agreements have been provided.</p>"
        },
        "title": "Fracturing Responsibility and Awareness of Chemicals Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6082.xml",
    "summary": {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fracturing Responsibility and Awareness of Chemicals Act of 2025</strong></p><p>This bill modifies drinking water requirements concerning hydraulic fracturing (fracking) operations, including by giving the Environmental Protection Agency (EPA) the authority to protect groundwater sources (e.g., wells) from certain pollution risks posed by fracking operations.</p><p>The bill also establishes requirements for disclosing the chemicals intended for use in fracking operations as well as the chemicals actually used in the operations. If the proprietary chemical formulas of chemicals used in fracking operations are necessary for treatment in medical emergencies, then the operations must disclose the formulas or the specific chemical identities of trade secret chemicals to the state, the EPA, or the treating physicians or nurses upon request, regardless of whether written statements of need or confidentiality agreements have been provided.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6082"
    },
    "title": "Fracturing Responsibility and Awareness of Chemicals Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fracturing Responsibility and Awareness of Chemicals Act of 2025</strong></p><p>This bill modifies drinking water requirements concerning hydraulic fracturing (fracking) operations, including by giving the Environmental Protection Agency (EPA) the authority to protect groundwater sources (e.g., wells) from certain pollution risks posed by fracking operations.</p><p>The bill also establishes requirements for disclosing the chemicals intended for use in fracking operations as well as the chemicals actually used in the operations. If the proprietary chemical formulas of chemicals used in fracking operations are necessary for treatment in medical emergencies, then the operations must disclose the formulas or the specific chemical identities of trade secret chemicals to the state, the EPA, or the treating physicians or nurses upon request, regardless of whether written statements of need or confidentiality agreements have been provided.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6082"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6082ih.xml"
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
      "title": "Fracturing Responsibility and Awareness of Chemicals Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fracturing Responsibility and Awareness of Chemicals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal the exemption for hydraulic fracturing in the Safe Drinking Water Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:48:37Z"
    }
  ]
}
```
