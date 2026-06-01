# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7830?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7830
- Title: WELLS Act
- Congress: 119
- Bill type: HR
- Bill number: 7830
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-05-13T08:06:33Z
- Update date including text: 2026-05-13T08:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7830",
    "number": "7830",
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
    "title": "WELLS Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:33Z",
    "updateDateIncludingText": "2026-05-13T08:06:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-05T15:01:45Z",
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
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "DC"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "OH"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "WI"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "LA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CT"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MD"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "LA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "GA"
    },
    {
      "bioguideId": "M001245",
      "district": "18",
      "firstName": "Christian",
      "fullName": "Rep. Menefee, Christian D. [D-TX-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Menefee",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IL"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MD"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "OH"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "HI"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "WA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NM"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NJ"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7830ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7830\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Ms. Kelly of Illinois (for herself, Mrs. Watson Coleman , Ms. Clarke of New York , Mrs. McIver , Ms. Norton , Ms. Sewell , Ms. Brown , Ms. Moore of Wisconsin , Mrs. Foushee , Ms. Wilson of Florida , Ms. Tlaib , Ms. Ansari , Mr. Tonko , Mr. Fields , Mrs. Cherfilus-McCormick , and Mr. Davis of Illinois ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to require hospitals to develop discharge plans for pregnant individuals as a condition of participation under Medicare, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Women Expansion of Learning and Labor Safety Act or the WELLS Act .\n#### 2. Requiring hospitals participating in Medicare to develop discharge plans for pregnant individuals\nSection 1866 of the Social Security Act ( 42 U.S.C. 1395cc ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin subparagraph (X), by striking and at the end;\n**(B)**\nin subparagraph (Y), by striking the period at the end and inserting , and ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(Z) beginning January 1, 2027, in the case of a hospital, critical access hospital, or rural emergency hospital, to comply with the requirements described in subsection (l)(1). ; and\n**(2)**\nby adding at the end the following new subsection:\n(l) Discharge plan requirements for pregnant individuals (1) In general For purposes of subsection (a)(1)(Z), the requirements described in this paragraph are, with respect to a hospital, critical access hospital, or rural emergency hospital, that the hospital\u2014 (A) provides for the development and implementation of a discharge plan meeting the standards under paragraph (2) with respect to any individual (whether or not eligible for benefits under this title) admitted to the hospital who\u2014 (i) is identified as pregnant; (ii) is experiencing signs or symptoms consistent with labor, which may include contractions; and (iii) is expected to be discharged from the hospital, critical access hospital, or rural emergency hospital prior to delivery, as determined based on the documented clinical judgment of the treating physician or practitioner at the time that such discharge is contemplated; (B) includes such discharge plan in the individual\u2019s medical record; and (C) provides for such discharge plan to be discussed with the individual (or the individual\u2019s representative) prior to discharge. (2) Discharge plan standards A discharge plan for an individual described in paragraph (1)(A) meets the standards under this paragraph if such plan includes at least the following information: (A) A clinical justification for the discharge. (B) An assessment of travel distance and time between the primary residence of the individual and the hospital, critical access hospital, or rural emergency hospital. (C) Verification of reliable transportation between the primary residence of the individual and the hospital, critical access hospital, or rural emergency hospital. (D) Identification of a back-up hospital or facility at which such individual may obtain labor and delivery services. (E) Confirmation that the plan was reviewed and approved by a qualified medical professional (as defined by the Secretary through regulations). (F) Confirmation that the individual (or the individual\u2019s representative) has received the information described in subparagraphs (A) through (D), that such information was provided in the primary language of such individual (or representative), and that such individual (or representative) confirmed their understanding of such information. (3) Rule of construction Nothing in this subsection shall be construed as limiting or otherwise affecting the discharge planning requirements otherwise applicable to a hospital, critical access hospital, or rural emergency hospital under this title. .\n#### 3. Rural maternal and obstetric care training demonstration grants\n##### (a) In general\nThe first section 764 of the Public Health Service Act ( 42 U.S.C. 294s ; relating to rural maternal and obstetric care training demonstration) is amended\u2014\n**(1)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(C)**\nby inserting after subparagraph (A) the following:\n(B) shall use the grant funds to provide racial bias training as part of such training program; and ;\n**(2)**\nby redesignating subsections (d) and (e) as subsections (e) and (f), respectively;\n**(3)**\nby inserting after subsection (c) the following:\n(d) Minimum performance milestones (1) Establishment Beginning with the grants awarded under this section for fiscal year 2027, the Secretary shall establish minimum performance milestones that grant recipients must meet during a fiscal year as a condition of remaining eligible for funding through such a grant for any subsequent fiscal year. (2) Milestones related to percent of staff trained The minimum performance milestones referred to in paragraph (1) shall include milestones related to the percent of all staff of the grant recipient that are trained, or that receive refresher training, with support from a grant under this section. ; and\n**(4)**\nin subsection (e), as so redesignated\u2014\n**(A)**\nin the subsection heading, by striking report and inserting reports ;\n**(B)**\nin paragraph (1)(B), by striking the report described in paragraph (2) and inserting the reports described in paragraphs (2) and (3) ; and\n**(C)**\nby adding at the end the following:\n(3) Subsequent reports Not later than January 1, 2027, and annually thereafter, the Secretary shall submit to Congress, and make publicly available, a report that includes\u2014 (A) updates to the information described in subparagraphs (A) through (C) of paragraph (2); and (B) additional information regarding the grants under this section, including\u2014 (i) a list of the entities receiving such grants; (ii) the number and amount of such grants; (iii) whether training supported by such grants was delivered in-person, virtually, asynchronously, or through some other format; and (iv) descriptions of the geographical coverage of such grants, the number of providers trained under such grants, and patient-level metrics linked to such training (such as changes in clinical outcomes, patient experience, and racial disparities). .\n##### (b) Technical amendment\nThe second section 764 of the Public Health Service Act ( 42 U.S.C. 294t ; relating to programs to promote mental health among the health professional workforce) is redesignated as section 764A.\n#### 4. Multi-center implementation science initiative for maternal health\nThe Secretary of Health and Human Services, in consultation with the Director of the Agency for Healthcare Research and Quality and the Director of the National Institutes of Health, shall establish a multi-center implementation science initiative for maternal health to rigorously evaluate different training models for health care professionals (including in-person, virtual, simulation, and cohort-based) and the impact of such models on provider behavior, patient outcomes, and maternal health disparities.\n#### 5. Maternal health dashboard\nThe Secretary of Health and Human Services shall develop, maintain, and make publicly available on the websites of the Department of Health and Human Services an interagency maternal health dashboard, which shall include maternal health outcome metrics from agencies within the Department of Health and Human Services and the data collected as part of the initiative under section 4, such as data related to maternal mortality and severe maternal morbidity, the number and outcomes of discharges of pregnant individuals prior to delivery from institutions, and data on Federal investments in maternal health research.",
      "versionDate": "2026-03-05",
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
        "updateDate": "2026-04-01T14:32:57Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7830ih.xml"
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
      "title": "WELLS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T03:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WELLS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Women Expansion of Learning and Labor Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to require hospitals to develop discharge plans for pregnant individuals as a condition of participation under Medicare, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T03:03:21Z"
    }
  ]
}
```
