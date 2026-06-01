# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1332?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1332
- Title: Aquatic Biodiversity Preservation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1332
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-07-11T08:05:23Z
- Update date including text: 2025-07-11T08:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1332",
    "number": "1332",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Aquatic Biodiversity Preservation Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-11T08:05:23Z",
    "updateDateIncludingText": "2025-07-11T08:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MD"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "HI"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "HI"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1332ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1332\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Min (for himself, Ms. Brownley , and Ms. Elfreth ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of Commerce to establish and carry out a program to sequence the genomes of aquatic species.\n#### 1. Short title\nThis Act may be cited as the Aquatic Biodiversity Preservation Act of 2025 .\n#### 2. Aquatic species genome sequencing program\n##### (a) In general\nThe Secretary shall establish and carry out a program to sequence the genomes of aquatic species, in coordination with covered entities, to enhance scientific understanding and conservation, management, and enforcement efforts with respect to such species.\n##### (b) Program duties\nIn carrying out the Program, the Secretary shall carry out activities that include the following:\n**(1)**\nIdentify and catalogue vouchered specimens, verifiably identified by a taxonomist, of aquatic species held by covered entities for the purpose of including such aquatic species in the Program.\n**(2)**\nObtain genetic samples, including through purchase or field collection, of priority species.\n**(3)**\nExtract and process DNA from samples of aquatic species or the environment through laboratory analysis, including carrying out any labor and acquiring any supplies required for such analysis.\n**(4)**\nSequence the genomes of aquatic species to accepted completeness and quality standards for reference genomes, including, as the Secretary determines appropriate, nuclear, mitochondrial, and chloroplast DNA.\n**(5)**\nCollect, catalogue, and store the metadata created by sequencing the genomes of aquatic species under paragraph (4).\n**(6)**\nMake publicly available the genomes and associated metadata of aquatic species that have been sequenced but are not publicly available.\n**(7)**\nProvide funding and technical assistance to covered entities that the Secretary determines appropriate to carry out the activities described in paragraphs (1) through (6).\n**(8)**\nEstablish principles for the management and sharing of data collected and produced through the Program in accordance with the document titled The FAIR Guiding Principles for scientific data management and stewardship (published March 15, 2016).\n##### (c) Program participation by covered entities\nA covered entity may carry out the activities described in paragraphs (1) through (6) of subsection (b) pursuant to the Program.\n##### (d) Data sharing\n**(1) In general**\nExcept as provided in paragraph (2), if the Secretary or a covered entity sequences the genome of an aquatic species pursuant to the Program, not later than 360 days after the date on which the sequencing of such genome is completed, the Secretary or the covered entity that sequenced such genome, as applicable, shall submit to the National Center for Biotechnology Information to make publicly available such sequenced genome and any associated raw sequence data and metadata, including\u2014\n**(A)**\nthe species of such genome;\n**(B)**\nthe location of where the sample that was used to sequence such genome was collected;\n**(C)**\nthe time and date of when such sample was collected;\n**(D)**\nthe process by which such genome was sequenced; and\n**(E)**\nany information required pursuant to the principles for the management and sharing of data collected and produced through the Program established under subsection (b)(8).\n**(2) Exception for Tribal governments**\nIf, pursuant to the Program, a Tribal Government sequences the genome of an aquatic species or provides a sample of an aquatic species to the Secretary that the Secretary uses to sequence the genome of such species, the Tribal Government shall be the only entity with the authority to determine whether and when to submit to the National Center for Biotechnology Information to make publicly available the data collected and produced through such sequencing.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out the Program $2,000,000 for each of fiscal years 2025 through 2031.\n##### (f) Definitions\nIn this section:\n**(1) Aquatic species of greatest conservation need**\nThe term aquatic species of greatest conservation need means an aquatic species that, unless otherwise specified, the Secretary determines requires conservation attention because such species\u2014\n**(A)**\nhas a low or declining population;\n**(B)**\nis facing threats; or\n**(C)**\nis considered by a Tribal Government or Native Hawaiian organization to be biologically or culturally significant for indigenous purposes.\n**(2) Covered entity**\nThe term covered entity means\u2014\n**(A)**\na Federal agency;\n**(B)**\na State Government;\n**(C)**\na Tribal Government;\n**(D)**\na Native Hawaiian organization;\n**(E)**\na nonprofit organization; and\n**(F)**\nan institution of higher education.\n**(3) Harmful algal bloom**\nThe term harmful algal bloom has the meaning given the term in section 609 of the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 ( 33 U.S.C. 4008 ).\n**(4) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(5) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(6) Native Hawaiian organization**\nThe term Native Hawaiian organization \u2014\n**(A)**\nmeans an organization that\u2014\n**(i)**\nserves and represents the interests of Native Hawaiians;\n**(ii)**\nhas as a primary and stated purpose the provision of services to Native Hawaiians; and\n**(iii)**\nhas expertise in Native Hawaiian affairs; and\n**(B)**\nincludes Native Hawaiian organizations registered with the Office of Native Hawaiian Relations of the Department of the Interior.\n**(7) Nonprofit organization**\nThe term nonprofit organization means an organization\u2014\n**(A)**\ndescribed in section 501(c)(3) of the Internal Revenue Code of 1986; and\n**(B)**\nthat is exempt from taxation under section 501(a) of that Code.\n**(8) Priority species**\nThe term priority species means an aquatic species\u2014\n**(A)**\nthe genome of which has not been fully sequenced or is not publicly available; and\n**(B)**\nthat is\u2014\n**(i)**\nlisted as a threatened species or as an endangered species pursuant to section 4 of the Endangered Species Act of 1973 ( 16 U.S.C. 1533 );\n**(ii)**\nincluded in the Non-indigenous Aquatic Species database of the United States Geological Survey;\n**(iii)**\nlisted in 1 of the Appendices of the Convention on International Trade in Endangered Species of Wild Fauna and Flora;\n**(iv)**\na macroinvertebrate that acts as a biological indicator of aquatic ecosystem health;\n**(v)**\na species that contributes to harmful algal blooms or a foodborne illness derived from eating seafood;\n**(vi)**\na species of fish that is managed pursuant to the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 );\n**(vii)**\nan aquatic species of greatest conservation need;\n**(viii)**\na species protected under the Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1361 et seq. );\n**(ix)**\na species monitored under the Seafood Import Monitoring Program of the National Marine Fisheries Service; or\n**(x)**\na look-alike species or a species that is morphologically or genetically closely related to a species described in clauses (i) through (x).\n**(9) Program**\nThe term Program means the program established under subsection (a).\n**(10) Secretary**\nThe term Secretary means the Secretary of Commerce.\n**(11) State**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, the Virgin Islands of the United States, and any other territory or possession of the United States.\n**(12) Tribal Government**\nThe term Tribal Government means the recognized governing body of an Indian Tribe.\n##### (g) Effective date\nThis section shall take effect on the date that is 180 days after the date of the enactment of this section.",
      "versionDate": "2025-02-13",
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
        "name": "Animals",
        "updateDate": "2025-03-18T21:04:39Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1332ih.xml"
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
      "title": "Aquatic Biodiversity Preservation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Aquatic Biodiversity Preservation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Commerce to establish and carry out a program to sequence the genomes of aquatic species.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:25Z"
    }
  ]
}
```
