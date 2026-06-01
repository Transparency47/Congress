# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/789?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/789
- Title: Critical Minerals Security Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 789
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-03-12 - Committee: Committee on Energy and Natural Resources. Hearings held. Hearings printed: S.Hrg. 119-46.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-03-12 - Committee: Committee on Energy and Natural Resources. Hearings held. Hearings printed: S.Hrg. 119-46.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/789",
    "number": "789",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Critical Minerals Security Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Hearings held. Hearings printed: S.Hrg. 119-46.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
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
            "date": "2025-03-12T15:58:45Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-12T15:58:45Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-27T18:23:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "VA"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-27",
      "state": "ME"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "OK"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s789is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 789\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Cornyn (for himself, Mr. Warner , Mr. Young , Mr. Hickenlooper , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require reports on critical mineral and rare earth element resources around the world and a strategy for the development of advanced mining, refining, separation, and processing technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Critical Minerals Security Act of 2025 .\n#### 2. Reports on critical mineral and rare earth element resources\n##### (a) Definitions\nIn this section:\n**(1) Covered nation**\nThe term covered nation has the meaning given the term in section 4872(d) of title 10, United States Code.\n**(2) Critical mineral**\nThe term critical mineral has the meaning given the term in section 7002(a) of the Energy Act of 2020 ( 30 U.S.C. 1606(a) ).\n**(3) Foreign entity of concern**\nThe term foreign entity of concern has the meaning given the term in section 40207(a) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18741(a) ).\n**(4) Rare earth elements**\nThe term rare earth elements means cerium, dysprosium, erbium, europium, gadolinium, holmium, lanthanum, lutetium, neodymium, praseodymium, promethium, samarium, scandium, terbium, thulium, ytterbium, and yttrium.\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior\n**(6) United states person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States; or\n**(B)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity.\n##### (b) Reports on critical mineral and rare earth element resources\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, and every 2 years thereafter, the Secretary, in consultation with the Secretary of Energy and the heads of other relevant Federal agencies, shall submit to Congress a report on all critical mineral and rare earth element resources (including recyclable or recycled materials containing those resources) around the world that includes\u2014\n**(A)**\nan assessment of\u2014\n**(i)**\nwhich of those resources are under the control of a foreign entity of concern, including through ownership, contract, or economic or political influence;\n**(ii)**\nwhich of those resources are owned by, controlled by, or subject to the jurisdiction or direction of the United States or a country that is an ally or partner of the United States;\n**(iii)**\nwhich of those resources are not owned by, controlled by, or subject to the jurisdiction or direction of a foreign entity of concern or a country described in clause (ii); and\n**(iv)**\nin the case of those resources not undergoing commercial mining, the reasons for the lack of commercial mining;\n**(B)**\nfor each mine from which significant quantities of critical minerals or rare earth elements are being extracted, as of the date that is 1 year before the date of the report\u2014\n**(i)**\nan estimate of the annual volume of output of the mine as of that date;\n**(ii)**\nan estimate of the total volume of mineral or elements that remain in the mine as of that date;\n**(iii)**\n**(I)**\nan identification of the country and entity operating the mine; or\n**(II)**\nif the mine is operated by more than 1 country or entity, an estimate of the output of each mineral or element from the mine to which each such country or entity has access; and\n**(iv)**\nan identification of the ultimate beneficial owners of the mine and the percentage of ownership held by each such owner;\n**(C)**\nfor each mine not described in subparagraph (B), to the extent practicable\u2014\n**(i)**\nan estimate of the aggregate annual volume of output of the mines as of the date that is 1 year before the date of the report;\n**(ii)**\nan estimate of the aggregate total volume of mineral or elements that remain in the mines as of that date; and\n**(iii)**\nan estimate of the aggregate total output of each mineral or element from the mine to which a foreign entity of concern has access;\n**(D)**\n**(i)**\na list of key foreign entities of concern involved in mining critical minerals and rare earth elements;\n**(ii)**\na list of key entities in the United States and countries that are allies or partners of the United States involved in mining critical minerals and rare earth elements; and\n**(iii)**\nan assessment of the technical feasibility of entities listed under clauses (i) and (ii) mining and processing resources identified under subparagraph (A)(iii) using existing advanced technology;\n**(E)**\nan assessment, prepared in consultation with the Secretary of State, of ways to collaborate with countries in which mines, mineral processing operations, or recycling operations (or any combination thereof) are located that are operated by other countries, or are operated by entities from other countries, to ensure ongoing access by the United States and countries that are allies and partners of the United States to those mines and processing or recycling operations;\n**(F)**\na list, prepared in consultation with the Secretary of Commerce, identifying, to the maximum extent practicable, all cases in which entities were forced to divest stock in mining, processing, or recycling operations (or any combination thereof) for critical minerals and rare earth elements based on\u2014\n**(i)**\nregulatory rulings of the government of a covered nation;\n**(ii)**\njoint regulatory rulings of the government of a covered nation and the government of another country; or\n**(iii)**\nrulings of a relevant tribunal or other entity authorized to render binding decisions on divestiture;\n**(G)**\na list of all cases in which the government of a covered nation purchased an entity that was forced to divest stock as described in subparagraph (F); and\n**(H)**\na list of all cases in which mining, processing, or recycling operations (or any combination thereof) for critical minerals and rare earth elements that were not subject to a ruling described in subparagraph (F) were taken over by\u2014\n**(i)**\nthe government of a covered nation; or\n**(ii)**\nan entity located in, or influenced or controlled by, the government of a covered nation.\n**(2) Form of report**\nEach report required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex, if necessary.\n##### (c) Process for notifying United States Government of divestment\nNot later than 1 year after the date of enactment of this Act, the Secretary, in consultation with the Secretary of State, shall establish a process under which\u2014\n**(1)**\na United States person seeking to divest stock in mining, processing, or recycling operations for critical minerals and rare earth elements in a foreign country may notify the Secretary of the intention of the person to divest the stock; and\n**(2)**\nthe Secretary may provide assistance to the person to find a purchaser that is not under the control of the government of a covered nation.\n##### (d) Strategy on development of advanced mining, refining, separation, processing, and recycling technologies\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary, in consultation with the Secretary of Energy and the heads of other relevant Federal agencies, shall develop\u2014\n**(A)**\na strategy to collaborate with the governments of countries that are allies and partners of the United States to develop advanced mining, refining, separation, processing, and recycling technologies; and\n**(B)**\na method for sharing the intellectual property resulting from the development of advanced mining, refining, separation, processing, and recycling technologies with the governments of countries that are allies and partners of the United States to enable those countries to license those technologies and mine, refine, separate, process, and recycle the resources of those countries.\n**(2) Reports required**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretary shall submit to Congress a report on the progress made in developing the strategy and method described in paragraph (1).",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-04-01T14:26:54Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-01T14:26:54Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-04-01T14:26:54Z"
          },
          {
            "name": "Metals",
            "updateDate": "2025-04-01T14:26:54Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-04-01T14:26:54Z"
          },
          {
            "name": "Strategic materials and reserves",
            "updateDate": "2025-04-01T14:26:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-11T14:38:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s789",
          "measure-number": "789",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s789v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Critical Minerals Security Act of 2025</strong></p><p>This bill establishes requirements for the Department of the Interior related to securing U.S. access to critical minerals and rare earth element (REE) resources.\u00a0<em>Critical minerals</em> mean any mineral, element, substance, or material designated as critical by the U.S. Geological Survey.\u00a0<em>REEs</em> mean cerium, dysprosium, erbium, europium, gadolinium, holmium, lanthanum, lutetium, neodymium, praseodymium, promethium, samarium, scandium, terbium, thulium, ytterbium, and yttrium.\u00a0</p><p>First, Interior must report on the critical mineral and\u00a0REE resources, including recyclable or recycled materials containing those resources, around the world. Among other information, the\u00a0report must include an assessment of the\u00a0global ownership and supply of critical mineral and\u00a0REE resources. Interior must submit the report within a year and every two years thereafter.</p><p>Next, Interior must establish a process to assist a U.S. person\u2014a U.S. citizen, a non-U.S. National (alien under federal law) lawfully admitted for permanent residence, or an entity organized under U.S. laws\u2014seeking to divest stock in mining, processing, or recycling operations for critical minerals and\u00a0REEs in a foreign country with finding a purchaser that is not under the control of North Korea, China, Russia, or Iran.</p><p>Finally, Interior must develop (1) a strategy to collaborate with U.S. allies and partners to develop advanced mining, refining, separation, processing, and recycling technologies; and (2) a method for sharing related\u00a0intellectual property with U.S. allies and partners to enable those countries to license those technologies and develop their resources.</p>"
        },
        "title": "Critical Minerals Security Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s789.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Critical Minerals Security Act of 2025</strong></p><p>This bill establishes requirements for the Department of the Interior related to securing U.S. access to critical minerals and rare earth element (REE) resources.\u00a0<em>Critical minerals</em> mean any mineral, element, substance, or material designated as critical by the U.S. Geological Survey.\u00a0<em>REEs</em> mean cerium, dysprosium, erbium, europium, gadolinium, holmium, lanthanum, lutetium, neodymium, praseodymium, promethium, samarium, scandium, terbium, thulium, ytterbium, and yttrium.\u00a0</p><p>First, Interior must report on the critical mineral and\u00a0REE resources, including recyclable or recycled materials containing those resources, around the world. Among other information, the\u00a0report must include an assessment of the\u00a0global ownership and supply of critical mineral and\u00a0REE resources. Interior must submit the report within a year and every two years thereafter.</p><p>Next, Interior must establish a process to assist a U.S. person\u2014a U.S. citizen, a non-U.S. National (alien under federal law) lawfully admitted for permanent residence, or an entity organized under U.S. laws\u2014seeking to divest stock in mining, processing, or recycling operations for critical minerals and\u00a0REEs in a foreign country with finding a purchaser that is not under the control of North Korea, China, Russia, or Iran.</p><p>Finally, Interior must develop (1) a strategy to collaborate with U.S. allies and partners to develop advanced mining, refining, separation, processing, and recycling technologies; and (2) a method for sharing related\u00a0intellectual property with U.S. allies and partners to enable those countries to license those technologies and develop their resources.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s789"
    },
    "title": "Critical Minerals Security Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Critical Minerals Security Act of 2025</strong></p><p>This bill establishes requirements for the Department of the Interior related to securing U.S. access to critical minerals and rare earth element (REE) resources.\u00a0<em>Critical minerals</em> mean any mineral, element, substance, or material designated as critical by the U.S. Geological Survey.\u00a0<em>REEs</em> mean cerium, dysprosium, erbium, europium, gadolinium, holmium, lanthanum, lutetium, neodymium, praseodymium, promethium, samarium, scandium, terbium, thulium, ytterbium, and yttrium.\u00a0</p><p>First, Interior must report on the critical mineral and\u00a0REE resources, including recyclable or recycled materials containing those resources, around the world. Among other information, the\u00a0report must include an assessment of the\u00a0global ownership and supply of critical mineral and\u00a0REE resources. Interior must submit the report within a year and every two years thereafter.</p><p>Next, Interior must establish a process to assist a U.S. person\u2014a U.S. citizen, a non-U.S. National (alien under federal law) lawfully admitted for permanent residence, or an entity organized under U.S. laws\u2014seeking to divest stock in mining, processing, or recycling operations for critical minerals and\u00a0REEs in a foreign country with finding a purchaser that is not under the control of North Korea, China, Russia, or Iran.</p><p>Finally, Interior must develop (1) a strategy to collaborate with U.S. allies and partners to develop advanced mining, refining, separation, processing, and recycling technologies; and (2) a method for sharing related\u00a0intellectual property with U.S. allies and partners to enable those countries to license those technologies and develop their resources.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s789"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s789is.xml"
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
      "title": "Critical Minerals Security Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Critical Minerals Security Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require reports on critical mineral and rare earth element resources around the world and a strategy for the development of advanced mining, refining, separation, and processing technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:31Z"
    }
  ]
}
```
