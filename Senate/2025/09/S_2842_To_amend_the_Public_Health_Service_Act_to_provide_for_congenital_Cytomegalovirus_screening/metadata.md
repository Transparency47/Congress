# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2842?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2842
- Title: Stop CMV Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2842
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-03-18T11:03:18Z
- Update date including text: 2026-03-18T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2842",
    "number": "2842",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Stop CMV Act of 2025",
    "type": "S",
    "updateDate": "2026-03-18T11:03:18Z",
    "updateDateIncludingText": "2026-03-18T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-17",
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
            "date": "2025-09-17T19:53:55Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-17T19:53:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "KS"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "AZ"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2842is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2842\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Blumenthal (for himself, Mr. Marshall , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to provide for congenital Cytomegalovirus screening of newborns.\n#### 1. Short title\nThis Act may be cited as Stop CMV Act of 2025 .\n#### 2. Screening of congenital Cytomegalovirus\nPart A of title XI of the Public Health Service Act is amended by inserting after section 1116 ( 42 U.S.C. 300b\u201315 ) the following:\n1116A. Screening of congenital Cytomegalovirus (a) In general Each hospital or other health care entity caring for infants who are 21 days or less of age (as designated by the Secretary) may administer, or cause to have administered, to every such infant in its care a test for congenital Cytomegalovirus in accordance with this section. (b) Process (1) In general In carrying out this section, the chief executive officer for health in each State may prescribe standards and procedures for the administration of testing under subsection (a), including recording the results of such tests, tracking activities, conducting follow-up reviews, and carrying out educational activities. (2) Dissemination of information In carrying out this section, the chief executive officer for health in each State may prescribe standards and procedures setting forth the manner in which testing information is disseminated to a parent or guardian of the infant to be tested. (3) Failure to prescribe If a State has not prescribed standards and procedures that are approved as provided for in paragraph (4) by the date that is 2 years after the date of enactment of the Stop CMV Act of 2025 , the Discretionary Advisory Committee on Heritable Disorders in Newborns and Children established under section 1111 (referred to in this section as the Advisory Committee ) shall prescribe appropriate standards and procedures which may be implemented by such State. (4) Review and approval The standards and procedures prescribed under this subsection shall be subject to review and approval by the Advisory Committee. In reviewing or prescribing standards and procedures as required under this subsection, the Advisory Committee shall consider standards and procedures adopted in other States with respect to the screening of congenital Cytomegalovirus, the standards and procedures adopted in such State with respect to the screening of infants for other heritable diseases, and any scientific evidence the Advisory Committee considers relevant to provide for the screening of infants for congenital Cytomegalovirus. (c) Grants (1) Health Resources and Services Administration (A) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration, shall award grants to States that prescribe standards and procedures in accordance with paragraphs (1) and (2), to be distributed by the States to entities described in subsection (a) to administer tests in accordance with that subsection. (B) Authorization of appropriations There is authorized to be appropriated to carry out subparagraph (A) such sums as may be necessary for each of fiscal years 2026 and 2027. (2) Centers for disease control and prevention (A) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall award grants to, or enter into cooperative agreements with, States to provide technical assistance to State agencies or designated entities of States\u2014 (i) to develop, maintain, and improve data collection systems relating to congenital Cytomegalovirus; and (ii) to assist in the education and training of health care providers, patients, and the general public regarding the risk reduction or prevention, symptoms, diagnosis, and treatment of congenital Cytomegalovirus, including, as necessary, through the publication of scientific, evidence-based educational materials on internet webpages maintained by State agencies or designated entities of States. (B) Authorization of appropriations There is authorized to be appropriated to carry out subparagraph (A) such sums as may be necessary for each of fiscal years 2026 and 2027. (3) National Institutes of Health (A) In general The Director of the National Institutes of Health shall\u2014 (i) for the purposes of this section, establish a program, or expand existing programs, of research and development on the efficacy of new screening techniques and technology relating to congenital Cytomegalovirus, including clinical studies of screening methods, studies on efficacy of intervention, and related research; and (ii) establish a program, or expand existing programs, of research and development into congenital Cytomegalovirus diagnostics, prevention, treatments including public health awareness campaigns, risk reduction, and vaccine development, and cures or treatments (during pregnancy and after birth). (B) Funding The Director of the National Institutes of Health shall carry out subparagraph (A) using amounts available to the Director and not otherwise obligated. .\n#### 3. Advisory committee on heritable disorders in newborns and children\nSection 1111(b) of the Public Health Service Act ( 42 U.S.C. 300b\u201310(b) ) is amended\u2014\n**(1)**\nin paragraph (7) by striking and after the semicolon;\n**(2)**\nby redesignating paragraph (8) as paragraph (9); and\n**(3)**\nby inserting after paragraph (7) the following:\n(8) carry out activities under section 1116A; and .",
      "versionDate": "2025-09-17",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "5435",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop CMV Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-11-17T18:35:53Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2842is.xml"
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
      "title": "Stop CMV Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop CMV Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-02T04:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to provide for congenital Cytomegalovirus screening of newborns.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-02T04:18:15Z"
    }
  ]
}
```
