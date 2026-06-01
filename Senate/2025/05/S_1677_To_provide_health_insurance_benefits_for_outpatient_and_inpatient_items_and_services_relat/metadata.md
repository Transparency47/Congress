# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1677?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1677
- Title: Ensuring Lasting Smiles Act
- Congress: 119
- Bill type: S
- Bill number: 1677
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2026-05-20T11:03:28Z
- Update date including text: 2026-05-20T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1677",
    "number": "1677",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Ensuring Lasting Smiles Act",
    "type": "S",
    "updateDate": "2026-05-20T11:03:28Z",
    "updateDateIncludingText": "2026-05-20T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
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
            "date": "2026-03-19T14:00:22Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-08T16:55:04Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-08T16:55:04Z",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "IA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MN"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "AK"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NM"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NC"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-08",
      "state": "ME"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "KS"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "RI"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "IA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NJ"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "OR"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "AZ"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "AR"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-06-16",
      "state": "MT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "AZ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "MD"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "AK"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "WV"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MD"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "MA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "GA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NV"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "WV"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "DE"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "NY"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "PA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "VT"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MI"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "ME"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-11-05",
      "state": "FL"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "OR"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-01-05",
      "state": "CO"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "ND"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "MS"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "WA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "DE"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NH"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MN"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "HI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1677is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1677\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Ms. Baldwin (for herself, Ms. Ernst , Ms. Klobuchar , Ms. Murkowski , Mr. Luj\u00e1n , Mr. Tillis , Mr. King , Mr. Marshall , Mr. Reed , Mr. Grassley , Mr. Blumenthal , Mr. Booker , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide health insurance benefits for outpatient and inpatient items and services related to the diagnosis and treatment of a congenital anomaly or birth defect.\n#### 1. Short title\nThis Act may be cited as the Ensuring Lasting Smiles Act .\n#### 2. Coverage of congenital anomaly or birth defect\n##### (a) Public Health Service Act Amendments\nPart D of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ) is amended by adding at the end the following new section:\n2799A\u201311. Coverage of congenital anomaly or birth defect (a) Requirements for care and reconstructive treatment (1) In general A group health plan, and a health insurance issuer offering group or individual health insurance coverage, shall provide coverage for outpatient and inpatient items and services related to the diagnosis and treatment of a congenital anomaly or birth defect that primarily impacts the appearance or function of the eyes, ears, teeth, mouth, or jaw, consistent with paragraphs (2) and (3). (2) Financial requirements Any coverage provided under paragraph (1) under a group health plan or group or individual health insurance coverage may be subject to cost-sharing requirements (such as coinsurance, copayments, and deductibles), as required by the plan or issuer offering such coverage, that are no more restrictive than the predominant cost-sharing requirements applied to substantially all other medical and surgical benefits covered by the plan or coverage. (3) Applicable items and services (A) In general Except as provided in subparagraph (B), the items and services required under paragraph (1) to be covered by a group health plan or group or individual health insurance coverage offered by a health insurance issuer include\u2014 (i) any item or service to improve, repair, or restore any body part to achieve normal body functioning or appearance, or performed to approximate a normal appearance, as determined medically necessary by the treating physician (as defined in section 1861(r) of the Social Security Act), on account of a congenital anomaly or birth defect that primarily impacts the appearance or function of the eyes, ears, teeth, mouth, or jaw; and (ii) any treatment or diagnostic service with respect to any and all missing or abnormal body parts (including teeth, the oral cavity, and their associated structures), as determined medically necessary by the treating physician (as defined in section 1861(r) of the Social Security Act), including\u2014 (I) reconstructive services and procedures, and items and services related to any complications arising from such services and procedures; (II) adjunctive dental, orthodontic, or prosthodontic support from birth until the medical or surgical treatment of the defect or anomaly has been completed, including ongoing or subsequent treatment required to maintain function or approximate a normal appearance, notwithstanding any exclusions, limitations, or restrictions under the plan or health insurance coverage on coverage of dental, orthodontic, or prosthodontic items and services arising from other injuries or sicknesses; and (III) items and services related to secondary conditions and follow-up treatment associated with the underlying congenital anomaly or birth defect. (B) Exception The items and services required under this subsection to be covered by a group health plan or health insurance issuer offering group or individual health insurance coverage shall not include cosmetic surgery performed to reshape normal structures of the body to improve appearance or self-esteem, if such items and services are not furnished as a result of a medical determination of a congenital anomaly or birth defect. (b) Notice Beginning not later January 1, 2026, a group health plan or health insurance issuer offering group or individual health insurance coverage shall provide notice to each participant and beneficiary under such plan or coverage regarding the coverage required by this section in any documents describing services, in accordance with any regulations promulgated by the Secretary. (c) Definition In this section, the term congenital anomaly or birth defect means a structural or functional anomaly that occurs during intrauterine life, develops prenatally, and may be identified before birth, at birth, or later in life, and which may\u2014 (1) be caused by genetic or chromosomal disorders, embryotoxic or teratogenic environmental factors, nutrient deficiency, multifactorial inheritance, or be of an unknown cause; (2) manifest as abnormal anatomical structures; (3) manifest as physical, sensory, or cognitive functional disabilities; (4) manifest as syndromes, diseases, or other health problems; and (5) manifest as singular anomalies or in combination prenatally, at birth, or later in life. .\n##### (b) ERISA amendments\n**(1) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 is amended by adding at the end the following:\n726. Coverage of congenital anomaly or birth defect (a) Requirements for care and reconstructive treatment (1) In general A group health plan, and a health insurance issuer offering group health insurance coverage, shall provide coverage for outpatient and inpatient items and services related to the diagnosis and treatment of a congenital anomaly or birth defect that primarily impacts the appearance or function of the eyes, ears, teeth, mouth, or jaw, consistent with paragraphs (2) and (3). (2) Financial requirements Any coverage provided under paragraph (1) under a group health plan or group health insurance coverage offered by a health insurance issuer may be subject to cost-sharing requirements (such as coinsurance, copayments, and deductibles), as required by the plan or issuer offering such coverage, that are no more restrictive than the predominant cost-sharing requirements applied to substantially all other medical and surgical benefits covered by the plan or coverage. (3) Applicable items and services (A) In general Except as provided in subparagraph (B), the items and services required under paragraph (1) to be covered by a group health plan or group health insurance coverage offered by a health insurance issuer include\u2014 (i) any item or service to improve, repair, or restore any body part to achieve normal body functioning or appearance, or performed to approximate a normal appearance, as determined medically necessary by the treating physician (as defined in section 1861(r) of the Social Security Act), on account of a congenital anomaly or birth defect that primarily impacts the appearance or function of the eyes, ears, teeth, mouth, or jaw; and (ii) any treatment or diagnostic service with respect to any and all missing or abnormal body parts (including teeth, the oral cavity, and their associated structures), as determined medically necessary by the treating physician (as defined in section 1861(r) of the Social Security Act), including\u2014 (I) reconstructive services and procedures, and items and services related to any complications arising from such services and procedures; (II) adjunctive dental, orthodontic, or prosthodontic support from birth until the medical or surgical treatment of the defect or anomaly has been completed, including ongoing or subsequent treatment required to maintain function or approximate a normal appearance, notwithstanding any exclusions, limitations, or restrictions under the plan or health insurance coverage on coverage of dental, orthodontic, or prosthodontic items and services arising from other injuries or sicknesses; and (III) items and services related to secondary conditions and follow-up treatment associated with the underlying congenital anomaly or birth defect. (B) Exception The items and services required under this subsection to be covered by a group health plan or health insurance issuer offering group health insurance coverage shall not include cosmetic surgery performed to reshape normal structures of the body to improve appearance or self-esteem, if such items and services are not furnished as a result of a medical determination of a congenital anomaly or birth defect. (b) Notice Beginning not later than January 1, 2026, a group health plan or health insurance issuer offering group health insurance coverage shall provide notice to each participant and beneficiary under such plan or coverage regarding the coverage required by this section, in any documents describing services, in accordance with any regulations promulgated by the Secretary. (c) Definition In this section, the term congenital anomaly or birth defect means a structural or functional anomaly that occurs during intrauterine life, develops prenatally, and may be identified before birth, at birth, or later in life, and which may\u2014 (1) be caused by genetic or chromosomal disorders, embryotoxic or teratogenic environmental factors, nutrient deficiency, multifactorial inheritance, or be of an unknown cause; (2) manifest as abnormal anatomical structures; (3) manifest as physical, sensory, or cognitive functional disabilities; (4) manifest as syndromes, diseases, or other health problems; and (5) manifest as singular anomalies or in combination prenatally, at birth, or later in life. .\n**(2) Technical amendments**\n**(A)**\nSection 732(a) of such Act ( 29 U.S.C. 1191a(a) ) is amended by striking section 711 and inserting sections 711 and 726 .\n**(B)**\nThe table of contents in section 1 of such Act is amended by inserting after the item relating to section 725 the following new item:\nSec. 726. Coverage of congenital anomaly or birth defect. .\n##### (c) Internal Revenue Code amendments\n**(1) In general**\nSubchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n9826. Coverage of congenital anomaly or birth defect (a) Requirements for care and reconstructive treatment (1) In general A group health plan shall provide coverage for outpatient and inpatient items and services related to the diagnosis and treatment of a congenital anomaly or birth defect that primarily impacts the appearance or function of the eyes, ears, teeth, mouth, or jaw, consistent with paragraphs (2) and (3). (2) Financial requirements Any coverage provided under paragraph (1) under a group health plan may be subject to cost-sharing requirements (such as coinsurance, copayments, and deductibles), as required by the plan, that are no more restrictive than the predominant cost-sharing requirements applied to substantially all other medical and surgical benefits covered by the plan. (3) Applicable items and services (A) In general Except as provided in subparagraph (B), the items and services required under paragraph (1) to be covered by a group health plan include\u2014 (i) any item or service to improve, repair, or restore any body part to achieve normal body functioning or appearance, or performed to approximate a normal appearance, as determined medically necessary by the treating physician (as defined in section 1861(r) of the Social Security Act), on account of a congenital anomaly or birth defect that primarily impacts the appearance or function of the eyes, ears, teeth, mouth, or jaw; and (ii) any treatment or diagnostic service with respect to any and all missing or abnormal body parts (including teeth, the oral cavity, and their associated structures), as determined medically necessary by the treating physician (as defined in section 1861(r) of the Social Security Act), including\u2014 (I) reconstructive services and procedures, and items and services related to any complications arising from such services and procedures; (II) adjunctive dental, orthodontic, or prosthodontic support from birth until the medical or surgical treatment of the defect or anomaly has been completed, including ongoing or subsequent treatment required to maintain function or approximate a normal appearance, notwithstanding any exclusions, limitations, or restrictions under the plan on coverage of dental, orthodontic, or prosthodontic items and services arising from other injuries or sicknesses; and (III) items and services related to secondary conditions and follow-up treatment associated with the underlying congenital anomaly or birth defect. (B) Exception The items and services required under this subsection to be covered by a group health plan shall not include cosmetic surgery performed to reshape normal structures of the body to improve appearance or self-esteem, if such items and services are not furnished as a result of a medical determination of a congenital anomaly or birth defect. (b) Notice Beginning not later January 1, 2026, a group health plan shall provide notice to each participant and beneficiary under such plan or coverage regarding the coverage required by this section in any documents describing services, in accordance with any regulations promulgated by the Secretary. (c) Definition In this section, the term congenital anomaly or birth defect means a structural or functional anomaly that occurs during intrauterine life, develops prenatally, and may be identified before birth, at birth, or later in life, and which may\u2014 (1) be caused by genetic or chromosomal disorders, embryotoxic or teratogenic environmental factors, nutrient deficiency, multifactorial inheritance, or be of an unknown cause; (2) manifest as abnormal anatomical structures; (3) manifest as physical, sensory, or cognitive functional disabilities; (4) manifest as syndromes, diseases, or other health problems; and (5) manifest as singular anomalies or in combination prenatally, at birth, or later in life. .\n**(2) Clerical amendment**\nThe table of sections for such subchapter is amended by adding at the end the following new item:\nSec. 9826. Coverage of congenital anomaly or birth defect. .\n##### (d) Study and report on network adequacy\nThe Secretary of Health and Human Services shall conduct a study, and not later than December 31, 2027, submit a report to Congress, on the matters relating to access of services for coverage of outpatient and inpatient items and services related to the diagnosis and treatment of a congenital anomaly or birth defect that primarily impacts the appearance or function of the eyes, ears, teeth, mouth, or jaw. Such study and report shall\u2014\n**(1)**\nevaluate the sufficiency and accessibility of networks of providers that perform services related to the diagnosis and treatment of such congenital anomalies and birth defects under group health plans and group and individual health insurance coverage (as such terms are defined in section 2791 of the Public Health Service Act ( 42 U.S.C. 300gg\u201391 )); and\n**(2)**\nassess any change in out-of-pocket costs for patients, by procedure type, resulting from the coverage requirements under sections 2799A\u201311 of the Public Health Service Act, 726 of the Employee Retirement Income Security Act of 1974, and 9826 of the Internal Revenue Code of 1986, as added by this section, and any change in the overall procedure cost for such services.\n##### (e) Effective date\nThe amendments made by subsections (a), (b), and (c) shall apply with respect to plan years beginning on or after January 1, 2026.",
      "versionDate": "2025-05-08",
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
        "actionDate": "2025-05-08",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3277",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ensuring Lasting Smiles Act",
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
            "name": "Birth defects",
            "updateDate": "2026-04-06T19:37:08Z"
          },
          {
            "name": "Child health",
            "updateDate": "2026-04-06T19:37:22Z"
          },
          {
            "name": "Dental care",
            "updateDate": "2026-04-06T19:38:40Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-06T19:38:46Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2026-04-06T19:36:41Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-04-06T19:36:50Z"
          },
          {
            "name": "Home and outpatient care",
            "updateDate": "2026-04-06T19:37:00Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2026-04-06T19:37:15Z"
          },
          {
            "name": "Surgery and anesthesia",
            "updateDate": "2026-04-06T19:38:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-23T14:25:24Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1677is.xml"
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
      "title": "Ensuring Lasting Smiles Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Lasting Smiles Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide health insurance benefits for outpatient and inpatient items and services related to the diagnosis and treatment of a congenital anomaly or birth defect.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:18:16Z"
    }
  ]
}
```
