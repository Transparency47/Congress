# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5133?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5133
- Title: Patients’ Right to Know Their Medication Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5133
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2026-05-12T08:05:44Z
- Update date including text: 2026-05-12T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5133",
    "number": "5133",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B000668",
        "district": "2",
        "firstName": "Cliff",
        "fullName": "Rep. Bentz, Cliff [R-OR-2]",
        "lastName": "Bentz",
        "party": "R",
        "state": "OR"
      }
    ],
    "title": "Patients\u2019 Right to Know Their Medication Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:44Z",
    "updateDateIncludingText": "2026-05-12T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:05:20Z",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "ME"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "GA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "WA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "NE"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "AR"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NH"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "ME"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "WI"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5133ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5133\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Mr. Bentz (for himself and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act regarding the patient medication information required to be included in the labeling of prescription drugs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Patients\u2019 Right to Know Their Medication Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPrescription medications are important to the health and well-being of the American public.\n**(2)**\nAccording to the Centers for Disease Control and Prevention (CDC), 48.9 percent of Americans used at least one prescription drug in the past 30 days.\n**(3)**\nThe utilization of prescription drugs can subject patients to adverse drug events; therefore, patient safety is of the utmost importance.\n**(4)**\nStudies indicate that paper format patient medication information (PMI) can help protect patients and prevent the majority of costly adverse drug events.\n**(5)**\nIn addition to bolstering patient safety, the mandatory use of a standardized PMI provided to all patients in nonhospital settings could reduce costs associated with emergency room visits and hospital admissions related to adverse drug events by $14.6 to $26.2 billion dollars annually.\n**(6)**\nMany patients cannot access electronic versions of PMI, thereby necessitating a paper option.\n**(7)**\nThe Government Accountability Office found that relying on electronic labeling as a complete substitute for paper labeling could adversely impact public health.\n**(8)**\nA congressionally mandated paper PMI is needed because no standardized PMI in a single page, paper copy, proven patient-friendly format is currently available to patients or required by the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ).\n#### 3. Patient medication information for prescription drugs\n##### (a) In general\nChapter V of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 351 et seq. ) is amended by inserting after section 505G ( 21 U.S.C. 355h ) the following:\n505H. Patient medication information for prescription drugs (a) In general The Secretary shall issue regulations on the patient medication information that is required to be in the printed labeling of drugs subject to section 503(b)(1), including regulations regarding the authorship, content, format, color, printing, and dissemination requirements for such patient medication information. The Secretary shall issue final regulations pursuant to the preceding sentence not later than 1 year after the date of enactment of this section. (b) Content The regulations promulgated under subsection (a) shall require that the patient medication information with respect to a drug\u2014 (1) be scientifically accurate, include relevant patient safety information, and be approved by the Secretary; (2) be developed by manufacturers applying for approval of a drug under this section and approved as part of such application by the Secretary; (3) with respect to the language used and format\u2014 (A) utilize understandable plain language and include graphics and pictures when applicable; (B) be provided in a consistent, standardized format, minimum font size, and color for all drug products; (C) be supplied by such manufacturer in printed form on paper with processes and verifications that are consistent with Current Good Manufacturing Practice; and (D) not be promotional in tone or content; (4) contain at least\u2014 (A) the established name of the drug (or, if the drug is a biological product, the proper name of the biological product) and the national drug code for the drug; (B) indications for use approved by the Food and Drug Administration; (C) general directions for proper use; (D) contraindications, warnings, precautions, the most frequently occurring adverse reactions, and adverse reactions that are important for other reasons (such as because they are serious), especially with respect to certain subpopulations such as children, pregnant women, and the elderly; (E) measures patients may be able to take, if any, to reduce the side effects and risks of the drug; (F) information about when a patient should contact his or her health care professional; (G) instructions not to share medications, and, if applicable, key storage requirements and recommendations relating to proper disposal of any unused portion of the drug; (H) known clinically important interactions with other drugs, food, and other substances; (I) a statement of whether sufficient data are available concerning the use of the drug in specified subpopulations, such as women, pregnant women, lactating women, women and men of reproductive age, and pediatric, geriatric, racial, and ethnic minority groups; (J) the name of the manufacturer and a toll-free telephone number for consumers to contact the manufacturer of the drug; and (K) a current link to Form FDA 3500B for voluntary reporting for consumers of adverse events, product problems, and product use errors (or any successor form); and (5) be provided to a patient or agent of a patient in a printed format with each prescription dispensed, such that a drug labeled for distribution shall be accompanied by printed labeling physically on or within the packaging from which the drug is to be dispensed, in an adequate supply. (c) Timeliness, consistency, accuracy, and effectiveness The regulations promulgated under subsection (a) shall\u2014 (1) provide for timely reviews, approvals, and updates of patient medication information as new drugs and new information become available; (2) provide for updates, when appropriate, to help communicate information that is shared by similar products or drugs within classes of medication to avoid patient confusion and harm; (3) include specifications for language, graphics, format, color, and pictures required by subsection (b)(2), to be developed based upon documented patient research with one or more actual drug products that demonstrates improved patient learning and understanding of safe and effective medication use; and (4) be based on a demonstrated causal connection between the enhanced patient medication information required by the regulations and improved patient medication adherence and compliance for the purpose of reducing the cost of health care and improving desired medical outcomes. (d) Adequate supply For purposes of this section, the term adequate supply means, with respect to the provision of patient medication information, that the number of printed patient medical information is adequate for the distribution of one printed patient medical information per prescription in the case of packaging that contains a bulk amount of prescription drug units intended to supply multiple prescriptions. .\n##### (b) Misbranding offense\nSection 502 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352 ) is amended by adding at the end the following:\n(hh) If it is a drug subject to section 503(b)(1) and patient medication information is not provided in accordance with section 505H. .",
      "versionDate": "2025-09-04",
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
        "name": "Health",
        "updateDate": "2025-09-23T17:18:58Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5133ih.xml"
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
      "title": "Patients\u2019 Right to Know Their Medication Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Patients\u2019 Right to Know Their Medication Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act regarding the patient medication information required to be included in the labeling of prescription drugs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:39Z"
    }
  ]
}
```
