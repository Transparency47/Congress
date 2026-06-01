# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1343?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1343
- Title: Advancing Quantum Manufacturing Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1343
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-03-26T11:03:17Z
- Update date including text: 2026-03-26T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1343",
    "number": "1343",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Advancing Quantum Manufacturing Act of 2025",
    "type": "S",
    "updateDate": "2026-03-26T11:03:17Z",
    "updateDateIncludingText": "2026-03-26T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-08",
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
            "date": "2025-04-08T20:03:50Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-08T20:03:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "NM"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "WA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NY"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "UT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1343is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1343\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mrs. Blackburn (for herself and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo improve coordination between the Department of Energy and the National Science Foundation on activities carried out under the National Quantum Initiative Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Quantum Manufacturing Act of 2025 .\n#### 2. Coordination between Department of Energy and National Science Foundation on activities under National Quantum Initiative\n##### (a) In general\nSection 102 of the National Quantum Initiative Act ( 15 U.S.C. 8812 ) is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Liaison between Department of Energy and National Science Foundation The Director of the Coordination Office shall appoint a member of the staff of the Coordination Office to serve as a liaison between the Department of Energy and the National Science Foundation to ensure the coordination, and avoid unnecessary duplication, of the Department and the Foundation activities under the Program. .\n##### (b) Sense of Congress\nIt is the sense of Congress that activities and research carried out by the Department of Energy and the National Science Foundation should include, to the extent practicable, all quantum information science technologies, as well as critical quantum-enabling technologies, including\u2014\n**(1)**\ngate-based quantum computing;\n**(2)**\nannealing-based quantum computing;\n**(3)**\nquantum bit (qubit) technologies, including those based on\u2014\n**(A)**\ntopological materials;\n**(B)**\nphotons;\n**(C)**\ntrapped ions;\n**(D)**\nneutral atoms;\n**(E)**\nsilicon;\n**(F)**\nsuperconducting devices; and\n**(G)**\nany other viable quantum technology; and\n**(4)**\nquantum-enabling technologies, including\u2014\n**(A)**\nsingle photon sources;\n**(B)**\nlasers;\n**(C)**\nradio frequency, microwave, and other electronics;\n**(D)**\nelectron spin;\n**(E)**\ncryogenic technologies;\n**(F)**\nlow-disorder or low-defect materials development and fabrication; and\n**(G)**\nany other critical enabling technology.\n#### 3. Establishment of Manufacturing USA institute for quantum manufacturing\n##### (a) Definition of Manufacturing USA institute\nIn this section, the term Manufacturing USA institute has the meaning given such term in section 34(d) of the National Institute of Standards and Technology Act ( 15 U.S.C. 278s(d) ).\n##### (b) Establishment of Manufacturing USA institute\nThe Secretary of Commerce, acting through the Director of the National Institute of Standards and Technology, and in consultation with the Secretary of Energy, shall\u2014\n**(1)**\ndetermine the manufacturing capabilities necessary to produce reliable quantum components and systems at scale and the gaps in access to such capabilities; and\n**(2)**\nestablish, or award financial assistance, under section 34(e)(1) of the National Institute of Standards and Technology Act ( 15 U.S.C. 278s(e)(1) ) to plan, establish, or support, a Manufacturing USA institute that\u2014\n**(A)**\nprovides an end-to-end manufacturing ecosystem addressing quantum computing, quantum sensing, and quantum communication;\n**(B)**\nincludes within the end-to-end ecosystem provided pursuant to paragraph (1) the capability to design, fabricate, and test materials, devices, structures, and manufacturing processes for quantum technologies or systems, as well as the capacity to develop and create jobs for a coordinated advanced manufacturing and quantum engineering workforce;\n**(C)**\nprovides access to prototyping, both at research scale and commercial scale, for researchers and developers working on quantum component technologies and systems and manufacturing process innovations to facilitate the transition into scalable, cost-effective, and high-performing manufacturing capabilities;\n**(D)**\nsupports the development of a resilient quantum supply chain with an emphasis on key components and supply from allies of the United States, that enables quantum technologies, and increases the domestic production of goods critical to national security and economic competitiveness; and\n**(E)**\nsupports development of a workforce with skills relevant to manufacture of quantum components and systems.\n#### 4. Studies relating to National Quantum Initiative Program\n##### (a) Independent study on progress made by National Quantum Initiative Program\n**(1) Agreement**\nThe Director of the Office of Science and Technology Policy shall seek to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine (in this subsection the National Academies ) to perform the services covered by this section.\n**(2) Independent study**\nUnder an agreement between the Director and the National Academies under this subsection, the National Academies shall carry out an independent study to assess the progress made by the National Quantum Initiative Program in achieving the purposes set forth under section 3 of the National Quantum Initiative Act ( 15 U.S.C. 8802 ) and the goals of the Program, including with respect to sensing, communications, computing, and workforce development for near-term development and quantum applications.\n##### (b) Study on impediments to collaboration under National Quantum Initiative Program\n**(1) Study and report**\nNot later than 180 days after the date of the enactment of this Act, the consortium convened by the Director of the National Institute of Standards and Technology pursuant to section 201(b)(1) of the National Quantum Initiative Act ( 15 U.S.C. 8831(b)(1) ) shall\u2014\n**(A)**\nconduct a study\u2014\n**(i)**\non the impediments to collaboration under the National Quantum Initiative Program implemented pursuant to section 101(a) of such Act ( 15 U.S.C. 8811(a) ) between Multidisciplinary Centers for Quantum Research and Education established under section 302(a) of such Act ( 15 U.S.C. 8842(a) ), National Quantum Information Science Research Centers established and operated pursuant to section 402(a)(1) of such Act ( 15 U.S.C. 8852(a)(1) ), industry, and academia; and\n**(ii)**\nto develop recommendations for legislative action to eliminate or mitigate such impediments; and\n**(B)**\nsubmit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report on the findings of the consortium with respect to the study conducted pursuant to paragraph (1).\n**(2) Contents**\nThe report submitted under paragraph (1)(B) shall include the following:\n**(A)**\nAn overview of the current state of research being conducted under the National Quantum Initiative Program.\n**(B)**\nA breakdown of the funding under the Program for near-term quantum applications development, disaggregated by different quantum technologies, including computing (annealing and gate-model with the different types of qubit technologies), sensing, communication, and networking.\n**(C)**\nIdentification of potential risks in the research funded under the Program.",
      "versionDate": "2025-04-08",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-19T16:02:39Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1343is.xml"
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
      "title": "Advancing Quantum Manufacturing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advancing Quantum Manufacturing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve coordination between the Department of Energy and the National Science Foundation on activities carried out under the National Quantum Initiative Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:20Z"
    }
  ]
}
```
