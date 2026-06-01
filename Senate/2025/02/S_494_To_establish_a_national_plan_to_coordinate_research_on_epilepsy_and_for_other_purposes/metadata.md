# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/494?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/494
- Title: National Plan for Epilepsy Act
- Congress: 119
- Bill type: S
- Bill number: 494
- Origin chamber: Senate
- Introduced date: 2025-02-10
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in Senate
- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-10: Introduced in Senate

## Actions

- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/494",
    "number": "494",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "National Plan for Epilepsy Act",
    "type": "S",
    "updateDate": "2026-05-12T11:03:31Z",
    "updateDateIncludingText": "2026-05-12T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-10",
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
      "actionDate": "2025-02-10",
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
            "date": "2025-02-10T21:28:30Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-10T21:28:30Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "MN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "AR"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "NH"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NJ"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-10-01",
      "state": "IA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "WV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "NH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "DE"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "VA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "MD"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "NY"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "ME"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "WV"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s494is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 494\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2025 Mr. Schmitt (for himself, Ms. Klobuchar , Mr. Boozman , and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish a national plan to coordinate research on epilepsy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Plan for Epilepsy Act .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nEpilepsy is a brain disorder that causes recurring and unprovoked seizures and affects people of all ages, affecting nearly 3,000,000 adults and 456,000 children in the United States.\n**(2)**\nEpilepsy and seizures can develop in any person at any age. One in 26 people will develop a form of epilepsy in their lifetime, with people from all demographic groups and walks of life being impacted.\n**(3)**\nIn approximately half of all cases of epilepsy, the underlying cause of the disease is unknown.\n**(4)**\nEpilepsy is a spectrum disease comprised of many diagnoses and an ever-growing number of rare epilepsies. There are many different types of seizures and varying levels of seizure control.\n**(5)**\nOver 30 percent of people with epilepsy live with uncontrolled seizures.\n**(6)**\nIndividuals with epilepsy have a 3-times higher risk of early death than the general population and that risk is even higher for individuals with uncontrolled seizures.\n**(7)**\nThirty-two percent of adults with epilepsy are unable to work.\n**(8)**\nFifty-three percent of individuals with uncontrolled seizures live in households earning less than $25,000 per year.\n**(9)**\nHealth care costs associated with epilepsy and seizures exceed $54,000,000,000 per year in the United States.\n#### 3. Establishing a National Plan for Epilepsy\nPart B of title III of the Public Health Service Act ( 42 U.S.C. 243 et seq. ) is amended by adding at the end the following:\n320C. Programs relating to epilepsy (a) National Plan for Epilepsy (1) In general The Secretary shall carry out a national project, to be known as the National Plan for Epilepsy (referred to in this section as the National Plan ), to prevent, diagnose, treat, and cure epilepsy. (2) Activities In carrying out the National Plan, the Secretary shall\u2014 (A) establish, maintain, and periodically update an integrated national plan to prevent, diagnose, treat, and cure epilepsy; (B) provide information, including an estimate of the level of Federal investment in preventing, diagnosing, treating, and curing epilepsy; (C) coordinate research and services related to epilepsy, across all Federal agencies; (D) encourage the development of safe and effective treatments, strategies, and other approaches to prevent, diagnose, treat, and cure epilepsy or to enhance functioning and improve quality of life for individuals with epilepsy and their caregivers; (E) improve the\u2014 (i) early diagnosis of epilepsy; and (ii) coordination of the care and treatment of individuals living with epilepsy; (F) review the impact of epilepsy on the physical, mental, and social health of individuals living with epilepsy and their caregivers; (G) solicit public comments and consider consensus recommendations from collaborations in the epilepsy community; (H) carry out an annual assessment on progress of the activities described in this subsection; (I) coordinate with international bodies, to the degree possible, to integrate and inform the global mission to prevent, diagnose, treat, and cure epilepsy; and (J) carry out other such activities as the Secretary determines appropriate. (b) Annual assessment Not later than 2 years after the date of enactment of the National Plan for Epilepsy Act , and annually thereafter, the Secretary shall carry out an assessment of the Nation\u2019s progress in preparing for and responding to the escalating burden of epilepsy. Such assessment shall include\u2014 (1) recommendations for priority actions; (2) a description of the steps that have been, or should be, taken to implement such recommendations; and (3) such other items as the Secretary determines appropriate. (c) Advisory Council (1) In general The Secretary shall establish and maintain an Advisory Council on Epilepsy Research, Care, and Services (referred to in this section as the Advisory Council ) to advise the Secretary on epilepsy-related issues. (2) Membership The Advisory Council shall be comprised of\u2014 (A) representatives appointed by the Secretary from relevant Federal departments and agencies, including\u2014 (i) the National Institutes of Health; (ii) the Centers for Medicare & Medicaid Services; (iii) the Centers for Disease Control and Prevention; (iv) the Food and Drug Administration; (v) the Health Resources and Services Administration; (vi) the Department of Defense; and (vii) the Department of Veterans Affairs; and (B) expert non-Federal members appointed by the Secretary that reflect the diversity of epilepsy, including\u2014 (i) 4 individuals, each of whom is living with a different type of epilepsy; (ii) 2 family caregivers for individuals with epilepsy; (iii) 2 licensed or accredited health care providers supported by a relevant professional medical society, including at least 1 epileptologist or neurologist; (iv) 2 biomedical researchers with epilepsy-related expertise in basic, translational, or clinical population science or drug development science; and (v) 3 representatives from 3 separate nonprofit organizations directly connected with epilepsy that have demonstrated experience in epilepsy research or epilepsy patient care and other services. (3) Meetings (A) In general The Advisory Council shall meet at least once each quarter. (B) Meetings with other experts Not later than 2 years after the date of enactment of the National Plan for Epilepsy Act , and every 2 years thereafter, the Advisory Council shall convene a meeting of Federal and non-Federal organizations to discuss epilepsy research. (C) Public meetings All meetings of the Advisory Council shall be open to the public. (4) Reporting Not later than 18 months after the date of enactment of the National Plan for Epilepsy Act , and every 2 years thereafter, the Advisory Council shall provide to the Secretary and Congress a report containing\u2014 (A) an evaluation of all federally funded efforts in preventing, diagnosing, treating, and curing epilepsy, and the outcomes of such efforts; (B) recommendations for priority actions to better coordinate, expand, and better support Federal programs in order to better support people with epilepsy, epilepsy research, and data collection; (C) recommendations to\u2014 (i) provide effective, timely, and responsive diagnosis treatment and care to improve health outcomes and quality of life; (ii) foster research and innovation leading to more effective treatments and potential cures for epilepsy; (iii) strengthen data and information systems including better surveillance of epilepsy; (iv) increase public awareness about epilepsy and reduce stigma and discrimination; (v) increase access to expert and specialized care for people with epilepsy; (vi) eliminate access to care disparities experienced by individuals with epilepsy; (vii) prevent sudden unexpected death in epilepsy and other epilepsy-related mortalities; (viii) reduce the financial impact of epilepsy on families living with epilepsy; (ix) prevent epilepsy and promote healthy behaviors; and (x) an evaluation of the implementation of the National Plan, and its outcomes. (d) Annual reports The Secretary shall annually submit to Congress a report that includes\u2014 (1) an evaluation of all federally funded efforts in epilepsy research, prevention, diagnosis, treatment, clinical care, and institutional-, home-, and community-based programs, and the outcomes of such efforts; (2) recommendations for\u2014 (A) priority actions based on the most recent assessment submitted by the Secretary under subsection (b) and the recommendations contained in the most recent report of the Advisory Council under subsection (c)(4); (B) priority actions to improve all federally funded efforts in epilepsy research, prevention, diagnosis, treatment, clinical care, and institutional-, home-, and community-based programs; and (C) implementation steps to address priority actions described in subparagraphs (A) and (B); and (3) a description of the progress made in carrying out the National Plan. (e) Data sharing Agencies both within the Department of Health and Human Services and outside of such Department that have data relating to epilepsy shall share such data with the Secretary as necessary to enable the Secretary to complete the reports described in subsection (d). (f) Sunset This section shall cease to be effective on December 31, 2035. .",
      "versionDate": "2025-02-10",
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
        "actionDate": "2025-02-11",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1189",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "National Plan for Epilepsy Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-04-24T16:22:48Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-24T16:22:53Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T16:19:22Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-04-24T16:23:03Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-04-24T16:22:57Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2025-04-24T16:22:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T16:22:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119s494",
          "measure-number": "494",
          "measure-type": "s",
          "orig-publish-date": "2025-02-10",
          "originChamber": "SENATE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s494v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>National Plan for Epilepsy Act</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to establish a national plan, form an advisory council, and take other actions to address epilepsy. The requirements sunset on December 31, 2035.</p><p>Specifically, the bill requires\u00a0HHS to carry out a National Plan for Epilepsy to prevent, diagnose, treat, and cure epilepsy. In carrying out the plan,\u00a0HHS must implement activities such as coordinating research and services across all federal agencies and soliciting public comments.</p><p>Also,\u00a0HHS must establish an Advisory Council on Epilepsy Research, Care, and Services. The advisory council must report to\u00a0HHS and Congress every two years with an evaluation of federally funded efforts.</p><p>Additionally,\u00a0HHS must annually report to Congress with recommended actions based on its assessments of the nation\u2019s progress on epilepsy. </p>"
        },
        "title": "National Plan for Epilepsy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s494.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>National Plan for Epilepsy Act</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to establish a national plan, form an advisory council, and take other actions to address epilepsy. The requirements sunset on December 31, 2035.</p><p>Specifically, the bill requires\u00a0HHS to carry out a National Plan for Epilepsy to prevent, diagnose, treat, and cure epilepsy. In carrying out the plan,\u00a0HHS must implement activities such as coordinating research and services across all federal agencies and soliciting public comments.</p><p>Also,\u00a0HHS must establish an Advisory Council on Epilepsy Research, Care, and Services. The advisory council must report to\u00a0HHS and Congress every two years with an evaluation of federally funded efforts.</p><p>Additionally,\u00a0HHS must annually report to Congress with recommended actions based on its assessments of the nation\u2019s progress on epilepsy. </p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119s494"
    },
    "title": "National Plan for Epilepsy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>National Plan for Epilepsy Act</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to establish a national plan, form an advisory council, and take other actions to address epilepsy. The requirements sunset on December 31, 2035.</p><p>Specifically, the bill requires\u00a0HHS to carry out a National Plan for Epilepsy to prevent, diagnose, treat, and cure epilepsy. In carrying out the plan,\u00a0HHS must implement activities such as coordinating research and services across all federal agencies and soliciting public comments.</p><p>Also,\u00a0HHS must establish an Advisory Council on Epilepsy Research, Care, and Services. The advisory council must report to\u00a0HHS and Congress every two years with an evaluation of federally funded efforts.</p><p>Additionally,\u00a0HHS must annually report to Congress with recommended actions based on its assessments of the nation\u2019s progress on epilepsy. </p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119s494"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s494is.xml"
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
      "title": "National Plan for Epilepsy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "National Plan for Epilepsy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a national plan to coordinate research on epilepsy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:01Z"
    }
  ]
}
```
