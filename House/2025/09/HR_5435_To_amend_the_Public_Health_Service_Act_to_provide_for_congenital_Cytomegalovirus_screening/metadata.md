# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5435?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5435
- Title: Stop CMV Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5435
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2026-03-27T08:06:44Z
- Update date including text: 2026-03-27T08:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-17: Introduced in House

## Actions

- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5435",
    "number": "5435",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Stop CMV Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:44Z",
    "updateDateIncludingText": "2026-03-27T08:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T14:00:20Z",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "OH"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NJ"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "NH"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "IL"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MO"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "WA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "AZ"
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
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5435ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5435\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Mr. Lawler (for himself, Mr. Landsman , and Ms. Ross ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to provide for congenital Cytomegalovirus screening of newborns.\n#### 1. Short title\nThis Act may be cited as Stop CMV Act of 2025 .\n#### 2. Screening of congenital Cytomegalovirus\nPart A of title XI of the Public Health Service Act is amended by inserting after section 1116 ( 42 U.S.C. 300b\u201315 ) the following:\n1116A. Screening of congenital Cytomegalovirus (a) In general Each hospital or other health care entity caring for infants who are 21 days or less of age (as designated by the Secretary) may administer, or cause to have administered, to every such infant in its care a test for congenital Cytomegalovirus in accordance with this section. (b) Process (1) In general In carrying out this section, the chief executive officer for health in each State may prescribe standards and procedures for the administration of testing under subsection (a), including recording the results of such tests, tracking activities, conducting follow-up reviews, and carrying out educational activities. (2) Dissemination of information In carrying out this section, the chief executive officer for health in each State may prescribe standards and procedures setting forth the manner in which testing information is disseminated to a parent or guardian of the infant to be tested. (3) Failure to prescribe If a State has not prescribed standards and procedures that are approved as provided for in paragraph (4) by the date that is 2 years after the date of enactment of the Stop CMV Act of 2025 , the Discretionary Advisory Committee on Heritable Disorders in Newborns and Children established under section 1111 (referred to in this section as the Advisory Committee ) shall prescribe appropriate standards and procedures which may be implemented by such State. (4) Review and approval The standards and procedures prescribed under this subsection shall be subject to review and approval by the Advisory Committee. In reviewing or prescribing standards and procedures as required under this subsection, the Advisory Committee shall consider standards and procedures adopted in other States with respect to the screening of congenital Cytomegalovirus, the standards and procedures adopted in such State with respect to the screening of infants for other heritable diseases, and any scientific evidence the Advisory Committee considers relevant to provide for the screening of infants for congenital Cytomegalovirus. (c) Grants (1) Health Resources and Services Administration (A) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration (referred to in this paragraph as the Secretary ), shall award grants to States that prescribe standards and procedures in accordance with paragraphs (1) and (2), to be distributed by the States to entities described in subsection (a) to administer tests in accordance with that subsection. (B) Authorization of appropriations There is authorized to be appropriated to carry out subparagraph (A) such sums as may be necessary for each of fiscal years 2025 and 2026. (2) Centers for disease control and prevention (A) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall award grants to, or enter into cooperative agreements with, States to provide technical assistance to State agencies or designated entities of States\u2014 (i) to develop, maintain, and improve data collection systems relating to congenital Cytomegalovirus; and (ii) to assist in the education and training of health care providers, patients, and the general public regarding the risk reduction or prevention, symptoms, diagnosis, and treatment of congenital Cytomegalovirus, including, as necessary, through the publication of scientific, evidence-based educational materials on internet web pages maintained by State agencies or designated entities of States. (B) Authorization of appropriations There is authorized to be appropriated to carry out subparagraph (A) such sums as may be necessary for each of fiscal years 2025 and 2026. (3) National institutes of health The Director of the National Institutes of Health shall\u2014 (A) for the purposes of this section, establish a program, or expand existing programs, of research and development on the efficacy of new screening techniques and technology relating to congenital Cytomegalovirus, including clinical studies of screening methods, studies on efficacy of intervention, and related research; and (B) establish a program, or expand existing programs, of research and development into congenital Cytomegalovirus diagnostics, prevention, treatments including public health awareness campaigns, risk reduction, and vaccine development, and cures or treatments (during pregnancy and after birth). .\n#### 3. Advisory committee on heritable disorders in newborns and children\nSection 1111(b) of the Public Health Service Act ( 42 U.S.C. 300b\u201310(b) ) is amended\u2014\n**(1)**\nin paragraph (7) by striking and after the semicolon;\n**(2)**\nby redesignating paragraph (8) as paragraph (9); and\n**(3)**\nby inserting after paragraph (7) the following:\n(8) carry out activities under section 1116A; and .",
      "versionDate": "2025-09-17",
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
        "actionDate": "2025-09-17",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2842",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop CMV Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-11-17T18:35:13Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5435ih.xml"
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
      "title": "Stop CMV Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T04:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop CMV Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to provide for congenital Cytomegalovirus screening of newborns.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:17Z"
    }
  ]
}
```
