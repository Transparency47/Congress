# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1254?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1254
- Title: Rural Obstetrics Readiness Act
- Congress: 119
- Bill type: HR
- Bill number: 1254
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2026-05-15T08:07:28Z
- Update date including text: 2026-05-15T08:07:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1254",
    "number": "1254",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000385",
        "district": "2",
        "firstName": "Robin",
        "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
        "lastName": "Kelly",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Rural Obstetrics Readiness Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:28Z",
    "updateDateIncludingText": "2026-05-15T08:07:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:00:45Z",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "WA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "PA"
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
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "SC"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "WA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "MA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "NM"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CO"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "VA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "DE"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "KS"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "OR"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "WI"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "IN"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "IA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "PA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NH"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "WI"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WV"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "MI"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "ME"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-19",
      "state": "PA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "CA"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "ME"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "GU"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "IN"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1254ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1254\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Ms. Kelly of Illinois (for herself, Mrs. Kim , Ms. Schrier , and Mr. Meuser ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo improve obstetric emergency care.\n#### 1. Short title\nThis Act may be cited as the Rural Obstetrics Readiness Act .\n#### 2. Obstetric emergency training program\nSection 330O of the Public Health Service Act ( 42 U.S.C. 254c\u201321 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (4), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(5) developing, and facilitating access to, an evidence-based program to train practitioners in rural health care facilities without dedicated obstetric units to provide emergency obstetric services during pregnancy, labor, delivery, or the postpartum period, including training on how to prepare for, identify, stabilize, and safely transfer, as appropriate and within the scope of practice of an individual practitioner, a woman experiencing labor, delivery, obstetric hemorrhage, severe hypertension, cardiac conditions, perinatal mental health conditions, substance use, sepsis, or other conditions, as appropriate. ;\n**(2)**\nby redesignating subsections (c) and (d) as subsections (d) and (e), respectively;\n**(3)**\nby inserting after subsection (b) the following:\n(c) Training program for eligible practitioners in rural health care facilities A training program described in subsection (a)(5) shall include an assessment of obstetric training needs for rural health care facilities without dedicated obstetric units. In developing the training program, a recipient of a grant under such subsection shall\u2014 (1) work in consultation with at least one representative from a national medical society that has experience or expertise in rural health care delivery in each of the fields of gynecology and obstetrics, emergency medicine, family medicine, and anesthesiology; and (2) facilitate access to obstetric readiness training via regional training partnerships and technical assistance to rural health care facilities. ; and\n**(4)**\nin subsection (e), as so redesignated, by adding at the end the following: In addition to amounts appropriated under the previous sentence, for grants for the purpose described in subsection (a)(5), there are authorized to be appropriated $5,000,000 for the period of fiscal years 2026 through 2028 .\n#### 3. Grant funding for equipment and supplies\nPart D of title III of the Public Health Service Act ( 42 U.S.C. 254b et seq. ) is amended by inserting after section 330A\u20132 the following:\n330A\u20133. Program of support for obstetric services (a) In general The Secretary shall award grants, contracts, or cooperative agreements to eligible entities to integrate obstetric readiness training curriculum into rural health care settings, build workforce capacity, and purchase equipment necessary to manage obstetric emergencies. (b) Use of funds A recipient of funds under this section shall use such funds for the purpose described in subsection (a), which may include any of the following: (1) Purchasing or providing equipment and technical assistance to train practitioners who are not specialized in obstetrics in preparing for, identifying, stabilizing, and transferring, as appropriate and within the scope of practice of the practitioner, individuals experiencing obstetric emergencies. (2) Purchasing or providing equipment necessary to prepare for, identify, stabilize, or transfer, as appropriate, individuals experiencing obstetric emergencies. (3) Developing and carrying out protocols for transfer of patients to other facilities and network engagement with other facilities. (4) Hiring additional personnel or paying the salaries of personnel. (5) Establishing training opportunities to enable non-obstetric health professionals to gain exposure to, and expertise in, the delivery of obstetric services, including through clinical rotations, fellowships, or cross-training clinicians in other specialties. (6) Enabling clinical educators to coordinate, develop, and implement comprehensive interdisciplinary trainings, including team-based simulation training for providers who may need to respond to an obstetric emergency. (c) Eligible entities To be eligible to receive a grant under this section, an entity shall\u2014 (1) be\u2014 (A) a rural hospital, critical access hospital (as determined under section 1820(c)(2) of the Social Security Act), or a rural emergency hospital (as defined in section 1861(kkk)(2) of the Social Security Act) that is located in a maternity care health professional target area or a rural area (as defined by the Secretary); or (B) a consortium of 3 entities that includes at least 2 entities described in subparagraph (A); and (2) agree to carry out the program described in subsection (a), in coordination with other federally funded maternal and child health programs, to the extent practicable, and in consultation with other maternal and child health programs in the same geographic area. (d) Definitions In this section\u2014 (1) the term maternity care health professional target area means a primary care health professional shortage area that is experiencing a shortage of maternity health care professionals, as identified under section 332(k); and (2) the term rural area has the meaning given such term by the Federal Office of Rural Health Policy. (e) Authorization of appropriations To carry out this section, there is authorized to be appropriated $15,000,000 for the period of fiscal years 2026 through 2029. .\n#### 4. Pilot program for teleconsultation\nPart D of title III of the Public Health Service Act ( 42 U.S.C. 254b et seq. ), is amended by inserting after section 330A\u20133, as inserted by section 3, the following:\n330A\u20134. Pilot program for teleconsultation (a) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration and in consultation with the Administrator of the Centers for Medicare & Medicaid Services, shall award grants or cooperative agreements to States, political subdivisions of States, and Indian Tribes and Tribal organizations (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act) to support the provision of urgent maternal health care in rural facilities without a dedicated obstetric unit, including by\u2014 (1) supporting the development of statewide or regional maternal health care telehealth access programs; and (2) supporting the improvement of existing statewide or regional maternal health care telehealth access programs described in subsection (b). (b) Statewide or regional maternal health care telehealth access programs A maternal health care telehealth access program described in this section, with respect to which an award under subsection (a) may be used, shall\u2014 (1) be a statewide or regional network of maternal health care teams that provide urgent support to rural non-obstetric settings of care; (2) support and further develop organized State or regional networks of maternal health care teams to provide urgent consultative support to rural non-obstetric settings of care; (3) conduct an assessment of urgent maternal health consultation needs among providers in rural non-obstetric settings of care; (4) provide assurances that the physicians responsive to the teleconsultation line are credentialed within their employing facility and can provide consultation where the patient is receiving care consistent with State requirements to provide care to individuals experiencing labor, delivery, obstetric hemorrhage, severe hypertension in pregnancy and postpartum, cardiac conditions related to or exacerbated by pregnancy, perinatal mental health conditions, substance use during pregnancy or the postpartum period, sepsis during pregnancy or after pregnancy end, or other conditions, as appropriate; (5) provide rapid statewide or regional clinical telephone or telehealth consultations when requested between the maternal care teams and providers in rural emergency non-obstetric settings; and (6) provide information to health care providers about available maternal health services for people in the community and assist with referrals to specialty care and community or behavioral health resources. (c) Reporting An entity receiving an award under this section shall submit a report to the Secretary, in such manner and containing such information as the Secretary may require, not later than 18 months after initial receipt of the grant. (d) Authorization of appropriations To carry out this section, there is authorized to be appropriated $5,000,000 for the period of fiscal years 2026 through 2029. .\n#### 5. Study on obstetric units in rural areas\nThe Secretary of Health and Human Services shall\u2014\n**(1)**\nconduct a study that maps maternity ward closures and regional patterns of patient transport and examines models for regional partnerships for rural obstetric care; and\n**(2)**\nnot later than 3 years after the date of enactment of this Act, submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce and the Committee on Education and Workforce of the House of Representatives, a report on the results of the study conducted under paragraph (1).",
      "versionDate": "2025-02-12",
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
        "actionDate": "2026-03-19",
        "text": "Committee on Health, Education, Labor, and Pensions. Hearings held."
      },
      "number": "380",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rural Obstetrics Readiness Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-04-11T18:22:51Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-04-11T18:22:51Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-11T18:22:51Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-11T18:22:51Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-04-11T18:22:51Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-04-11T18:22:51Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-04-11T18:22:51Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-04-11T18:22:51Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-04-11T18:22:51Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-04-11T18:22:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T18:39:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1254",
          "measure-number": "1254",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-04-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1254v00",
            "update-date": "2025-04-30"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rural Obstetrics Readiness Act</strong></p><p>This bill creates and expands federal grant programs within the Health Resources and Services Administration (HRSA) to increase capacity to provide emergency obstetric health services in rural areas or areas without practitioners or facilities specializing in obstetric services.\u00a0</p><p>Specifically,\u00a0HRSA must establish a program for providing grants to certain hospitals or\u00a0consortiums that include hospitals in rural areas or areas with maternal health care professional shortages for training, developing a workforce, and purchasing equipment relating to obstetric emergencies. In addition, the bill requires\u00a0HRSA\u2019s Alliance for Innovation on Maternal Health Capacity program to provide grants for training on emergency obstetric services for practitioners in rural health care facilities without dedicated obstetric units. HRSA must also establish a pilot program to provide grants to government entities for developing or improving telehealth access programs to support urgent maternal health care in rural facilities without a dedicated obstetric unit.\u00a0</p>"
        },
        "title": "Rural Obstetrics Readiness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1254.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Obstetrics Readiness Act</strong></p><p>This bill creates and expands federal grant programs within the Health Resources and Services Administration (HRSA) to increase capacity to provide emergency obstetric health services in rural areas or areas without practitioners or facilities specializing in obstetric services.\u00a0</p><p>Specifically,\u00a0HRSA must establish a program for providing grants to certain hospitals or\u00a0consortiums that include hospitals in rural areas or areas with maternal health care professional shortages for training, developing a workforce, and purchasing equipment relating to obstetric emergencies. In addition, the bill requires\u00a0HRSA\u2019s Alliance for Innovation on Maternal Health Capacity program to provide grants for training on emergency obstetric services for practitioners in rural health care facilities without dedicated obstetric units. HRSA must also establish a pilot program to provide grants to government entities for developing or improving telehealth access programs to support urgent maternal health care in rural facilities without a dedicated obstetric unit.\u00a0</p>",
      "updateDate": "2025-04-30",
      "versionCode": "id119hr1254"
    },
    "title": "Rural Obstetrics Readiness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Obstetrics Readiness Act</strong></p><p>This bill creates and expands federal grant programs within the Health Resources and Services Administration (HRSA) to increase capacity to provide emergency obstetric health services in rural areas or areas without practitioners or facilities specializing in obstetric services.\u00a0</p><p>Specifically,\u00a0HRSA must establish a program for providing grants to certain hospitals or\u00a0consortiums that include hospitals in rural areas or areas with maternal health care professional shortages for training, developing a workforce, and purchasing equipment relating to obstetric emergencies. In addition, the bill requires\u00a0HRSA\u2019s Alliance for Innovation on Maternal Health Capacity program to provide grants for training on emergency obstetric services for practitioners in rural health care facilities without dedicated obstetric units. HRSA must also establish a pilot program to provide grants to government entities for developing or improving telehealth access programs to support urgent maternal health care in rural facilities without a dedicated obstetric unit.\u00a0</p>",
      "updateDate": "2025-04-30",
      "versionCode": "id119hr1254"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1254ih.xml"
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
      "title": "Rural Obstetrics Readiness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Obstetrics Readiness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T08:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve obstetric emergency care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T08:18:24Z"
    }
  ]
}
```
