# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7257?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7257
- Title: SECURE Grid Act
- Congress: 119
- Bill type: HR
- Bill number: 7257
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-05-27T18:41:27Z
- Update date including text: 2026-05-27T18:41:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-27 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-11 - Calendars: Placed on the Union Calendar, Calendar No. 561.
- 2026-05-11 - Committee: Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-644.
- 2026-05-11 - Committee: Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-644.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-27 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-11 - Calendars: Placed on the Union Calendar, Calendar No. 561.
- 2026-05-11 - Committee: Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-644.
- 2026-05-11 - Committee: Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-644.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7257",
    "number": "7257",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000566",
        "district": "5",
        "firstName": "Robert",
        "fullName": "Rep. Latta, Robert E. [R-OH-5]",
        "lastName": "Latta",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "SECURE Grid Act",
    "type": "HR",
    "updateDate": "2026-05-27T18:41:27Z",
    "updateDateIncludingText": "2026-05-27T18:41:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-05-11",
      "calendarNumber": {
        "calendar": "U00561"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 561.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-05-11",
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
      "text": "Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-644.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-644.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
        "item": [
          {
            "date": "2026-05-11T15:18:38Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-27T17:31:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-04T22:40:26Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-04T22:40:06Z",
                "name": "Markup by"
              },
              {
                "date": "2026-01-27T22:39:32Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
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
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "OH"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MI"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7257ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7257\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Latta (for himself and Ms. Matsui ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Energy Policy and Conservation Act to require States to include supporting the physical security, cybersecurity, and resilience of local distribution systems in State energy security plans.\n#### 1. Short title\nThis Act may be cited as the Securing Community Upgrades for a Resilient Grid Act or the SECURE Grid Act .\n#### 2. Consideration of the security of local distribution systems in State energy security plans\nSection 366 of the Energy Policy and Conservation Act ( 42 U.S.C. 6326 ) is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(3) Local distribution system The term local distribution system means any energy infrastructure owned and operated by an electric utility at a voltage of 100 kilovolts or less. ;\n**(2)**\nin subsection (b)(2), by inserting , and suppliers of equipment for the generation, transmission, and distribution of electricity to, after owners and operators of ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby amending paragraph (3) to read as follows:\n(3) address potential hazards to each energy sector or system, including\u2014 (A) physical threats and vulnerabilities, including\u2014 (i) weather-related threats and vulnerabilities; (ii) physical attacks on local distribution systems and the bulk-power system; and (iii) supply chain risks for equipment for the generation, transmission, and distribution of electricity; and (B) cybersecurity threats and vulnerabilities, including threats to, and vulnerabilities of, local distribution systems that may impact the bulk-power system; ; and\n**(B)**\nby amending paragraph (5) to read as follows:\n(5) provide a risk mitigation approach to enhance reliability and end-use resilience, including methods of responding to, mitigating, and recovering from potential hazards described in paragraph (3); and ;\n**(4)**\nin subsection (d)(3)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(C)**\nby inserting after subparagraph (A) the following:\n(B) supplying equipment for the generation and transmission of electricity; and ;\n**(5)**\nin subsection (e)\u2014\n**(A)**\nby striking A State is not eligible and inserting the following:\n(1) Submission required A State is not eligible ;\n**(B)**\nin paragraph (2), by redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively;\n**(C)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively; and\n**(D)**\nby adding at the end the following:\n(2) State determination A submission under paragraph (1) is not required to be approved by the Secretary. ;\n**(6)**\nin subsection (h), by inserting , local distribution system, after electric utility ; and\n**(7)**\nin subsection (i), by striking 2025 and inserting 2030 .",
      "versionDate": "2026-01-27",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7257rh.xml",
      "text": "IB\nUnion Calendar No. 561\n119th CONGRESS\n2d Session\nH. R. 7257\n[Report No. 119\u2013644]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Latta (for himself and Ms. Matsui ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nMay 11, 2026 Additional sponsors: Mr. Balderson , Mr. James , and Mr. Onder\nMay 11, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on January 27, 2026\nA BILL\nTo amend the Energy Policy and Conservation Act to require States to include supporting the physical security, cybersecurity, and resilience of local distribution systems in State energy security plans.\n#### 1. Short title\nThis Act may be cited as the Securing Community Upgrades for a Resilient Grid Act or the SECURE Grid Act .\n#### 2. Consideration of the security of local distribution systems in State energy security plans\nSection 366 of the Energy Policy and Conservation Act ( 42 U.S.C. 6326 ) is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(3) Local distribution system The term local distribution system means any energy infrastructure owned and operated by an electric utility at a voltage of 100 kilovolts or less. ;\n**(2)**\nin subsection (b)(2), by inserting , and suppliers of equipment for the generation, transmission, and distribution of electricity to, after owners and operators of ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby amending paragraph (3) to read as follows:\n(3) address potential hazards to each energy sector or system, including\u2014 (A) physical threats and vulnerabilities, including\u2014 (i) weather-related threats and vulnerabilities; (ii) physical attacks on local distribution systems and the bulk-power system; and (iii) supply chain risks for equipment for the generation, transmission, and distribution of electricity; and (B) cybersecurity threats and vulnerabilities, including threats to, and vulnerabilities of, local distribution systems that may impact the bulk-power system; ; and\n**(B)**\nby amending paragraph (5) to read as follows:\n(5) provide a risk mitigation approach to enhance reliability and end-use resilience, including methods of responding to, mitigating, and recovering from potential hazards described in paragraph (3); and ;\n**(4)**\nin subsection (d)(3)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(C)**\nby inserting after subparagraph (A) the following:\n(B) supplying equipment for the generation, transmission, and distribution of electricity; and ;\n**(5)**\nin subsection (e)\u2014\n**(A)**\nby striking A State is not eligible and inserting the following:\n(1) Submission required A State is not eligible ;\n**(B)**\nin paragraph (2), by redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively;\n**(C)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively (and by moving the margins accordingly); and\n**(D)**\nby adding at the end the following:\n(2) State determination A submission under paragraph (1) is not required to be approved by the Secretary. ;\n**(6)**\nin subsection (f), by striking may and inserting shall ;\n**(7)**\nin subsection (h), by inserting , local distribution system, after electric utility ; and\n**(8)**\nby striking subsection (i) and inserting the following:\n(i) Sunset This section shall expire on September 30, 2031. .\n#### 3. GAO Report\n##### (a) In general\nNot later than September 30, 2030, the Comptroller General shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Energy and Natural Resources of the Senate a report on the efficacy of State energy security plans that includes\u2014\n**(1)**\nan evaluation of whether and how State energy security plans have improved the ability of States to identify, assess, and mitigate risks to energy infrastructure and supply chains and to plan for, respond to, and recover from events that disrupt energy supply;\n**(2)**\nrecommendations for\u2014\n**(A)**\nimproving the ability of States described in paragraph (1); and\n**(B)**\nactions the Secretary of Energy may take to improve coordination with States with respect to identifying, assessing, and mitigating risks to energy infrastructure and supply chains and planning for, responding to, and recovering from events that disrupt energy supply;\n**(3)**\ninformation on Federal financial assistance made available to States under part D of title III of the Energy Policy and Conservation Act ( 42 U.S.C. 6321 et seq. ) that was used to implement State energy security plans;\n**(4)**\ninformation on activities carried out by States using such financial assistance;\n**(5)**\nan analysis of the efficacy of the implementation of section 366 of the Energy Policy and Conservation Act ( 42 U.S.C. 6326 ), as amended by this Act; and\n**(6)**\ninformation on State use of assistance provided under section 366(f) of the Energy Policy and Conservation Act ( 42 U.S.C. 6326(f) ) (as amended by this Act), including any revisions of State energy security plans made by States resulting from assistance provided under such section 366(f).\n##### (b) Protected information\nThe report required under subsection (a) shall be submitted in a form that may be made available to the public, except that any information protected from disclosure under section 366(h) of the Energy Policy and Conservation Act ( 42 U.S.C. 6326(h) ) shall be included in the report in an annex that shall not be publicly disclosed, consistent with such section.\n##### (c) State energy security plan defined\nIn this section, the term State energy security plan has the meaning given such term in section 366(a) of the Energy Policy and Conservation Act ( 42 U.S.C. 6326(a) ).",
      "versionDate": "2026-05-11",
      "versionType": "Reported in House"
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
        "actionDate": "2026-03-24",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "4166",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SECURE Grid Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-25T15:47:09Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-02-25T15:47:04Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-02-25T15:46:59Z"
          },
          {
            "name": "Public utilities and utility rates",
            "updateDate": "2026-02-25T15:47:29Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-25T15:51:28Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-08T15:39:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-05-18T20:39:55Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7257ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7257rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "SECURE Grid Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Securing Community Upgrades for a Resilient Grid Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "title": "SECURE Grid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SECURE Grid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Community Upgrades for a Resilient Grid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Energy Policy and Conservation Act to require States to include supporting the physical security, cybersecurity, and resilience of local distribution systems in State energy security plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:03:17Z"
    }
  ]
}
```
