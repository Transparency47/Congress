# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2623?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2623
- Title: Innovative Therapies Centers of Excellence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2623
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-04-21T08:06:29Z
- Update date including text: 2026-04-21T08:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-08 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-08 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2623",
    "number": "2623",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001110",
        "district": "46",
        "firstName": "J.",
        "fullName": "Rep. Correa, J. Luis [D-CA-46]",
        "lastName": "Correa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Innovative Therapies Centers of Excellence Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:29Z",
    "updateDateIncludingText": "2026-04-21T08:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-08T15:34:44Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "MI"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "TX"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "TX"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NV"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MD"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "WI"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "IL"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "MI"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "WA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "LA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "NJ"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "TX"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MS"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "KY"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "KY"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "AS"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "DE"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2623ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2623\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Correa (for himself, Mr. Bergman , Mr. Crenshaw , Mr. Khanna , and Mr. Luttrell ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the Secretary of Veterans Affairs to designate medical facilities of the Department of Veterans Affairs as innovative therapies centers of excellence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Innovative Therapies Centers of Excellence Act of 2025 .\n#### 2. Department of Veterans Affairs designation of innovative therapies centers of excellence\n##### (a) In general\nChapter 73 of title 38, United States Code, is amended by inserting after section 7330D the following new section:\n7330E. Innovative therapies centers of excellence (a) Establishment of centers (1) The Secretary, upon the recommendation of the Under Secretary for Health, shall designate not less than five Department medical facilities as the locations for innovative therapies centers of excellence. (2) Subject to the availability of appropriations for such purpose, the Secretary shall establish and operate innovative therapies centers of excellence at the locations designated pursuant to paragraph (1). (b) Geographic distribution of facilities In designating Department medical facilities as centers of excellence under subsection (a), the Secretary, upon the recommendation of the Under Secretary for Health, shall assure appropriate geographic distribution of such facilities. (c) Requirements for designation (1) The Secretary may not designate a Department medical facility as a location for a center under subsection (a) unless the peer review panel established under subsection (d) has determined under that subsection that the proposal submitted by such facility as a location for a new center under subsection (a) is among those proposals that meet the highest competitive standards of scientific and clinical merit. (2) The Secretary may not designate a Department medical facility as a location for a center under subsection (a) unless the Secretary, upon the recommendation of the Under Secretary for Health, determines that the facility has, or may reasonably be anticipated to develop, each of the following: (A) An arrangement with an\u2014 (i) accredited medical school that provides education and training in innovative therapies and with which the Department medical facility is affiliated under which residents receive education and training in use of innovative therapies to treat covered conditions; (ii) an accredited school of psychiatry; and (iii) an accredited school of social work. (B) The ability to attract the participation of scientists who are capable of ingenuity and creativity in medical research efforts. (C) An advisory committee composed of veterans and appropriate medical and research representatives of the Department medical facility and of the affiliated school or schools to advise the directors of such facility and such center on policy matters pertaining to the activities of the center during the period of the operation of such center. (D) The capability to conduct effectively evaluations of the activities of such center. (E) The capability to coordinate (as part of an integrated national system) education, clinical, and research activities within all facilities with such centers. (F) The capability to jointly develop a consortium of providers with interest in treating covered conditions with innovative therapies at Department facilities without such centers in order to ensure better access to state-of-the-art diagnosis, care, and education for innovative therapies throughout the medical system of the Department. (G) The capability to develop a national repository in the medical system of the Department for the collection of data on health services delivered to veterans seeking innovative therapies. (d) Peer review panel (1) The Under Secretary for Health shall establish a panel to assess the scientific and clinical merit of proposals that are submitted to the Secretary for the establishment of centers under this section. (2) (A) The membership of the panel shall consist of experts in innovative therapies. (B) Members of the panel shall serve for a period of no longer than two years, except as specified in subparagraph (C). (C) Of the members first appointed to the panel, one half shall be appointed for a period of three years and one half shall be appointed for a period of two years, as designated by the Under Secretary at the time of appointment. (3) The panel shall review each proposal submitted to the panel by the Under Secretary and shall submit its views on the relative scientific and clinical merit of each such proposal to the Under Secretary. (4) The panel shall not be subject to chapter 10 of title 5. (e) Annual report Not later than two years after the date of the enactment of this section, and annually thereafter, the Under Secretary of Health shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the activities of the centers of excellence designated under this section during the period covered by the report. Each such report shall include\u2014 (1) a summary of activities carried out by the centers during such period; (2) an identification of key findings made at such centers during such period; (3) recommendations to improve the delivery of innovative therapies to veterans; and (4) such other matters as the Under Secretary determines relevant. (f) Authorization of appropriations There are authorized to be appropriated $30,000,000 for each fiscal year for the support of the research and education activities of the centers established pursuant to subsection (a). The Under Secretary for Health shall allocate to such centers from other funds appropriated generally for the Department medical services account and medical and prosthetics research account, as appropriate, such amounts as the Under Secretary for Health determines appropriate. (g) Definitions In this section; (1) The term covered condition means any of the following: (A) Anxiety. (B) Bipolar disorder. (C) Chronic pain. (D) Depression. (E) Parkinson\u2019s disease. (F) Post-traumatic stress disorder. (G) Substance use disorder. (H) Such other conditions as may be designated by the Under Secretary. (2) The term innovative therapy means any of the following: (A) 3,4-Methylenedioxy-methamphetamine. (B) 5-Methoxy-N,N-dimethyltryptamine. (C) Ibogaine. (D) Ketamine. (E) Psilocybin. (F) Such other therapies as may be designated by the Under Secretary. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 7330D the following new item:\n7330E. Innovative therapies centers of excellence. .",
      "versionDate": "2025-04-03",
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
        "actionDate": "2026-03-09",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "4031",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Innovative Therapies Centers of Excellence Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T14:08:02Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2623ih.xml"
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
      "title": "Innovative Therapies Centers of Excellence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T08:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Innovative Therapies Centers of Excellence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T08:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require the Secretary of Veterans Affairs to designate medical facilities of the Department of Veterans Affairs as innovative therapies centers of excellence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T08:48:23Z"
    }
  ]
}
```
