# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2598?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2598
- Title: Forest Bioeconomy Act
- Congress: 119
- Bill type: S
- Bill number: 2598
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-18T20:30:35Z
- Update date including text: 2025-09-18T20:30:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2598",
    "number": "2598",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Forest Bioeconomy Act",
    "type": "S",
    "updateDate": "2025-09-18T20:30:35Z",
    "updateDateIncludingText": "2025-09-18T20:30:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T18:34:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "MT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "GA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2598is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2598\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Heinrich (for himself, Mr. Daines , Mr. Warnock , and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo expand research relating to the use of forest products, to support research and technologies of the Forest Service, and to establish a mass timber science and education program to respond to the emerging research needs of architects, developers, and the forest products industry.\n#### 1. Short title\nThis Act may be cited as the Forest Bioeconomy Act .\n#### 2. Bioeconomy research and technology transfer\n##### (a) Forest products research\nThe Secretary of Agriculture (referred to in this section as the Secretary ), in coordination with the Secretary of Energy, shall expand research relating to the use of wood\u2014\n**(1)**\nto facilitate the establishment of new markets, including nontraditional markets, for material produced from forest management projects that typically has little or no commercial value;\n**(2)**\nto increase the economic viability of manufacturing products using material described in paragraph (1); and\n**(3)**\nas a feedstock for the production of renewable fuel, including sustainable aviation fuel.\n##### (b) Office of Technology Transfer\n**(1) Establishment**\nThere is established within the Forest Service an Office of Technology Transfer (referred to this subsection as the Office ).\n**(2) Mission**\nThe mission of the Office shall be\u2014\n**(A)**\nto expand the commercial impact of the research investments of the Forest Service; and\n**(B)**\nto provide for the commercialization of technologies that support the mission of the Forest Service.\n**(3) Chief Commercialization Officer**\n**(A) In general**\nThe Office shall be headed by an officer, who shall\u2014\n**(i)**\nbe known as the Chief Commercialization Officer ; and\n**(ii)**\nreport to the Deputy Chief of the Forest Service for Research and Development.\n**(B) Qualifications**\nAn individual appointed to the position of Chief Commercialization Officer shall be an individual who, by reason of professional background and experience, is specially qualified to advise the Chief of the Forest Service and the Deputy Chief of the Forest Service for Research and Development on technology transfer at the Forest Service.\n**(C) Duties**\nThe Chief Commercialization Officer shall\u2014\n**(i)**\noversee the expenditure of funds allocated for technology transfer within the Forest Service;\n**(ii)**\nrepresent the Forest Service on\u2014\n**(I)**\nthe Federal Laboratory Consortium for Technology Transfer established by section 11(e) of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3710(e) ); and\n**(II)**\nother similar interagency coordinating entities;\n**(iii)**\ncoordinate with\u2014\n**(I)**\nother technology transfer and commercialization offices within the Department of Agriculture; and\n**(II)**\nother similar Federal entities, as appropriate;\n**(iv)**\noversee efforts to engage with private sector entities, including venture capital companies, on issues relating to technology transfer and commercialization; and\n**(v)**\ncoordinate efforts to patent or otherwise protect under title 35, United States Code, any inventions arising from a Forest Service laboratory.\n**(4) Technology Transfer Working Group**\n**(A) Establishment**\nThe Secretary shall establish within the Forest Service a Technology Transfer Working Group, which shall consist of\u2014\n**(i)**\nthe Deputy Chief of the Forest Service for Research and Development;\n**(ii)**\nthe Chief Commercialization Officer appointed under paragraph (3);\n**(iii)**\nrepresentatives from each research station within the Forest Service; and\n**(iv)**\nrepresentatives from other Forest Service entities with relevant expertise, as appropriate.\n**(B) Duties**\nThe Technology Transfer Working Group established under subparagraph (A) shall\u2014\n**(i)**\nassist with the coordination of technology transfer and commercialization opportunities occurring at Forest Service laboratories;\n**(ii)**\ndevelop and disseminate guidance to researchers at Forest Service laboratories on technology transfer and commercialization requirements under the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3701 et seq. ) and associated agreements to implement those requirements; and\n**(iii)**\ndevelop and disseminate to the public and prospective technology partners information about opportunities and procedures for technology transfer with the Forest Service.\n**(C) Report**\nNot later than 1 year after the date of enactment of this Act, the Technology Transfer Working Group established under subparagraph (A) shall submit to Congress a report that describes\u2014\n**(i)**\nthe number of cooperative research and development agreements entered into by the Forest Service under section 12 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3710a ) during the preceding 5 years;\n**(ii)**\nthe number of agreements with partnership intermediaries entered into by the Forest Service under section 23 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3715 ) during the preceding 5 years;\n**(iii)**\nthe number of licenses and other use authorizations issued by the Forest Service for patents held by the Forest Service during the preceding 5 years; and\n**(iv)**\nrecommendations for legislative, programmatic, or regulatory changes to support the mission of the Office.\n**(5) Key performance indicators**\nBeginning with the first year after the report under paragraph (4)(C) is submitted, and each year thereafter, the President shall include in the budget of the United States Government submitted to Congress under section 1105 of title 31, United States Code\u2014\n**(A)**\nthe number of cooperative research and development agreements entered into by the Forest Service under section 12 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3710a ) during the preceding year;\n**(B)**\nthe number of agreements with partnership intermediaries entered into by the Forest Service under section 23 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3715 ) during the preceding year; and\n**(C)**\nthe number of licenses or other use authorizations issued by the Forest Service for patents held by the Forest Service during the preceding year.\n**(6) Authorization of appropriations**\nThere is authorized to be appropriated to the Secretary to carry out this subsection $5,000,000 for each fiscal year.\n##### (c) National Forest Foundation activities\nSection 402(b)(3) of the National Forest Foundation Act ( 16 U.S.C. 583j(b)(3) ) is amended by striking cooperative forestry and inserting technology transfer, commercialization, cooperative forestry, .\n##### (d) Small business voucher pilot program\n**(1) Establishment**\nThe Secretary, in consultation with the Secretary of Energy and the Administrator of the Small Business Administration, shall establish an innovation voucher pilot program to accelerate product development, demonstration, and commercialization in the forest products sector.\n**(2) Vouchers**\nUnder the pilot program established under paragraph (1), the Secretary shall provide vouchers to small business concerns (as defined in section 3 of the Small Business Act ( 15 U.S.C. 632 )) to be used at research facilities of the Forest Service for research, development, demonstration, technology transfer, skills training and workforce development, or commercial application activities.\n**(3) Cost sharing**\n**(A) Basic research**\nThe Secretary may require up to 20 percent of the cost of a voucher provided under paragraph (2) for a research or development activity that is of a basic or fundamental nature, at the discretion of the Secretary, to be provided by a non-Federal source.\n**(B) Applied research**\nExcept as provided in subparagraph (D), the Secretary shall require not less than 20 percent of the cost of a voucher provided under paragraph (2) for a research or development activity that is not of a basic or fundamental nature, at the discretion of the Secretary, to be provided by a non-Federal source.\n**(C) Demonstration and commercial application**\nExcept as provided in subparagraph (D), the Secretary shall require not less than 50 percent of the cost of a voucher provided under paragraph (2) for a demonstration or commercial application activity to be provided by a non-Federal source.\n**(D) Reduction in cost-share**\nThe Secretary may reduce a non-Federal share required under subparagraph (B) or (C) if the Secretary determines the reduction to be necessary and appropriate, taking into account any technological risk relating to the activity.\n**(4) Termination**\nThe authorities provided under this subsection (except for paragraph (5)) shall expire on September 30, 2031.\n**(5) Report**\nNot later than 180 days after the termination of the pilot program under paragraph (4), the Secretary shall submit to Congress a report describing the outcomes of the pilot program, including any recommendations to improve the pilot program.\n#### 3. Joint mass timber science and education program\n##### (a) Definitions\nIn this section:\n**(1) Mass timber**\nThe term mass timber includes\u2014\n**(A)**\ncross-laminated timber;\n**(B)**\nnail laminated timber;\n**(C)**\nglue laminated timber;\n**(D)**\ndowel laminated timber;\n**(E)**\nlaminated strand lumber; and\n**(F)**\nlaminated veneer lumber.\n**(2) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Deputy Chief of the Forest Service for Research and Development.\n**(3) Tall wood building**\nThe term tall wood building means a building designed to be\u2014\n**(A)**\nconstructed with mass timber; and\n**(B)**\n**(i)**\nin the case of a residential building, more than 4 stories in height; or\n**(ii)**\nin the case of a commercial building, more than 5 stories in height.\n##### (b) Mass timber science and education program\nThe Secretary shall establish a mass timber science and education program to respond to the emerging research needs of architects, real estate developers, and the forest products industry.\n##### (c) Coordination\nThe Secretary shall coordinate with research programs at colleges and universities in administering the mass timber science and education program established under subsection (b) to supplement the current research and educational efforts of colleges and universities.\n##### (d) Purposes\nThe mass timber science and education program established under subsection (b) shall have the following principal purposes:\n**(1)**\nTo provide practical research responsive to the needs of architects, real estate developers, and the forest products industry, including assessments of carbon impacts in the originating forests and the end use of mass timber in the built environment.\n**(2)**\nTo develop focused, strategic lines of new research responsive to the needs described in paragraph (1), including research relating to flammability and performance during a fire, structural characteristics, energy use and savings, acoustics, and slab construction composed of hybrid materials.\n**(3)**\nTo solicit competitive funding proposals from scientists selected through a rigorous peer-review process designed to ensure the best projects are funded.\n**(4)**\nTo disseminate research findings so that architects, real estate developers, and the forest products industry are aware of, understand, and can use the information to make sound decisions and implement projects.\n**(5)**\nTo develop and facilitate the voluntary adoption of a curriculum for building structures using mass timber for use in schools of engineering and architecture that includes\u2014\n**(A)**\nstructural design; and\n**(B)**\nthe possibilities, benefits, and limitations of using mass timber in construction.\n##### (e) Mass timber strategy\nNot later than September 30, 2026, the Secretary shall submit to the relevant committees of Congress a strategy to carry out the mass timber science and education program established under subsection (b) that includes\u2014\n**(1)**\nan assessment of the current state of knowledge about mass timber and tall wood buildings;\n**(2)**\nan integrated approach to improve knowledge sharing on the manufacturing and use of mass timber products;\n**(3)**\nan approach for mass timber project monitoring and evaluation; and\n**(4)**\nan approach for setting research priorities for the program.\n##### (f) Stakeholder advisory group\n**(1) Membership**\nThe Secretary shall appoint a stakeholder advisory group of technical experts that consists, at a minimum, of\u2014\n**(A)**\na Forest Service scientist;\n**(B)**\na researcher from a college or university;\n**(C)**\na representative of a trade association;\n**(D)**\nan architect or real estate developer;\n**(E)**\na representative of an agency or unit of a local government that is responsible for the issuance of permits for building construction (commonly known as a local approving agency );\n**(F)**\na representative of a forest products company; and\n**(G)**\na representative of a nongovernmental organization with experience\u2014\n**(i)**\ndesigning or constructing tall wood buildings; or\n**(ii)**\ncomplying with or revising related building codes.\n**(2) Duties**\nThe stakeholder advisory group shall meet at least annually\u2014\n**(A)**\nto consider immediate and long-term science needs relating to the use of mass timber and the construction of tall wood buildings;\n**(B)**\nto suggest to the Secretary appropriate topic areas, specific issues within those topic areas, and information transfer needs for which the Secretary shall solicit proposals described in subsection (d)(3); and\n**(C)**\nto assist the Secretary in drafting the strategy required under subsection (e).\n##### (g) Availability of appropriations\nFrom amounts appropriated for Forest Service research, excluding funding made available for the Forest Inventory and Analysis program, the Secretary may use not more than $4,000,000 to carry out the activities described in this section.",
      "versionDate": "2025-07-31",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-18T20:30:35Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2598is.xml"
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
      "title": "Forest Bioeconomy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Forest Bioeconomy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand research relating to the use of forest products, to support research and technologies of the Forest Service, and to establish a mass timber science and education program to respond to the emerging research needs of architects, developers, and the forest products industry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:23Z"
    }
  ]
}
```
