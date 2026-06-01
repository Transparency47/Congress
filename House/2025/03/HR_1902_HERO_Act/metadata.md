# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1902?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1902
- Title: HERO Act
- Congress: 119
- Bill type: HR
- Bill number: 1902
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2026-04-24T08:06:58Z
- Update date including text: 2026-04-24T08:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1902",
    "number": "1902",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001287",
        "district": "6",
        "firstName": "Ami",
        "fullName": "Rep. Bera, Ami [D-CA-6]",
        "lastName": "Bera",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "HERO Act",
    "type": "HR",
    "updateDate": "2026-04-24T08:06:58Z",
    "updateDateIncludingText": "2026-04-24T08:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-06T14:06:40Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IN"
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
      "sponsorshipDate": "2025-03-06",
      "state": "DC"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "FL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "WI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NJ"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "RI"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NJ"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NE"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NV"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "WA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MI"
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
      "sponsorshipDate": "2025-03-06",
      "state": "OH"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "WA"
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
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MD"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
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
      "sponsorshipDate": "2026-03-25",
      "state": "NC"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
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
      "sponsorshipDate": "2026-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MN"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1902ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1902\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Bera (for himself, Mr. Fitzpatrick , Mr. Mrvan , Ms. Norton , Ms. Dean of Pennsylvania , Ms. Wasserman Schultz , Ms. Chu , Mr. Harder of California , Mr. Pocan , Mrs. Watson Coleman , Mr. Magaziner , Mr. Van Drew , Mr. Huffman , Mr. Lynch , Mr. Kennedy of New York , Mr. Casten , Mr. Panetta , Mr. Bacon , Mr. Latimer , Ms. Titus , Mr. Smith of Washington , Mr. Thanedar , Ms. Brown , and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Health and Human Services to improve the detection, prevention, and treatment of mental health issues among public safety officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Emergency Responders Overcome Act or the HERO Act .\n#### 2. Data system to capture national public safety officer suicide incidence\nThe Public Health Service Act is amended by inserting after section 317V of such Act ( 42 U.S.C. 247b\u201324 ) the following:\n317W. Data system to capture national public safety officer suicide incidence (a) In general The Secretary, in coordination with the Director of the Centers for Disease Control and Prevention and other agencies as the Secretary determines appropriate, may\u2014 (1) develop and maintain a data system, to be known as the Public Safety Officer Suicide Reporting System, for the purposes of\u2014 (A) collecting data on the suicide incidence among public safety officers; and (B) facilitating the study of successful interventions to reduce suicide among public safety officers; and (2) integrate such system into the National Violent Death Reporting System, so long as the Secretary determines such integration to be consistent with the purposes described in paragraph (1). (b) Data collection In collecting data for the Public Safety Officer Suicide Reporting System, the Secretary shall, at a minimum, collect the following information: (1) The total number of suicides in the United States among all public safety officers in a given calendar year. (2) Suicide rates for public safety officers in a given calendar year, disaggregated by\u2014 (A) age and gender of the public safety officer; (B) State; (C) occupation; including both the individual\u2019s role in their public safety agency and their primary occupation in the case of volunteer public safety officers; (D) where available, the status of the public safety officer as volunteer, paid-on-call, or career; and (E) status of the public safety officer as active or retired. (c) Consultation during development In developing the Public Safety Officer Suicide Reporting System, the Secretary shall consult with non-Federal experts to determine the best means to collect data regarding suicide incidence in a safe, sensitive, anonymous, and effective manner. Such non-Federal experts shall include, as appropriate, the following: (1) Public health experts with experience in developing and maintaining suicide registries. (2) Organizations that track suicide among public safety officers. (3) Mental health experts with experience in studying suicide and other profession-related traumatic stress. (4) Clinicians with experience in diagnosing and treating mental health issues. (5) Active and retired volunteer, paid-on-call, and career public safety officers. (6) Relevant national police, and fire and emergency medical services, organizations. (d) Data privacy and security In developing and maintaining the Public Safety Officer Suicide Reporting System, the Secretary shall ensure that all applicable Federal privacy and security protections are followed to ensure that\u2014 (1) the confidentiality and anonymity of suicide victims and their families are protected, including so as to ensure that data cannot be used to deny benefits; and (2) data is sufficiently secure to prevent unauthorized access. (e) Reporting (1) Annual report Not later than 2 years after the date of enactment of the Helping Emergency Responders Overcome Act , and biannually thereafter, the Secretary shall submit a report to the Congress on the suicide incidence among public safety officers. Each such report shall\u2014 (A) include the number and rate of such suicide incidence, disaggregated by age, gender, and State of employment; (B) identify characteristics and contributing circumstances for suicide among public safety officers; (C) disaggregate rates of suicide by\u2014 (i) occupation; (ii) status as volunteer, paid-on-call, or career; and (iii) status as active or retired; (D) include recommendations for further study regarding the suicide incidence among public safety officers; (E) specify in detail, if found, any obstacles in collecting suicide rates for volunteers and include recommended improvements to overcome such obstacles; (F) identify options for interventions to reduce suicide among public safety officers; and (G) describe procedures to ensure the confidentiality and anonymity of suicide victims and their families, as described in subsection (d)(1). (2) Public availability Upon the submission of each report to the Congress under paragraph (1), the Secretary shall make the full report publicly available on the website of the Centers for Disease Control and Prevention. (f) Definition In this section, the term public safety officer means\u2014 (1) a public safety officer, as defined in section 1204 of the Omnibus Crime Control and Safe Streets Act of 1968; or (2) a public safety telecommunicator, as described in detailed occupation 43\u20135031 in the Standard Occupational Classification Manual of the Office of Management and Budget (2018). (g) Prohibited use of information Notwithstanding any other provision of law, if an individual is identified as deceased based on information contained in the Public Safety Officer Suicide Reporting System, such information may not be used to deny or rescind life insurance payments or other benefits to a survivor of the deceased individual. .\n#### 3. Peer-support behavioral health and wellness programs within fire departments and emergency medical service agencies\n##### (a) In general\nPart B of title III of the Public Health Service Act ( 42 U.S.C. 243 et seq. ) is amended by adding at the end the following:\n320C. Peer-support behavioral health and wellness programs within fire departments and emergency medical service agencies (a) In general The Secretary may award grants to eligible entities for the purpose of establishing or enhancing peer-support behavioral health and wellness programs within fire departments and emergency medical services agencies. (b) Program description A peer-support behavioral health and wellness program funded under this section shall\u2014 (1) use career and volunteer members of fire departments or emergency medical services agencies to serve as peer counselors; (2) provide training to members of career, volunteer, and combination fire departments or emergency medical service agencies to serve as such peer counselors; (3) purchase materials to be used exclusively to provide such training; and (4) disseminate such information and materials as are necessary to conduct the program. (c) Definition In this section: (1) The term eligible entity means a nonprofit organization with expertise and experience with respect to the health and life safety of members of fire and emergency medical services agencies. (2) The term member \u2014 (A) with respect to an emergency medical services agency, means an employee, regardless of rank or whether the employee receives compensation (as defined in section 1204(7) of the Omnibus Crime Control and Safe Streets Act of 1968); and (B) with respect to a fire department, means any employee, regardless of rank or whether the employee receives compensation, of a Federal, State, Tribal, or local fire department who is responsible for responding to calls for emergency service. .\n##### (b) Technical correction\nEffective as if included in the enactment of the Children\u2019s Health Act of 2000 ( Public Law 106\u2013310 ), the amendment instruction in section 1603 of such Act is amended by striking Part B of the Public Health Service Act and inserting Part B of title III of the Public Health Service Act .\n#### 4. Health care provider behavioral health and wellness programs\nPart B of title III of the Public Health Service Act ( 42 U.S.C. 243 et seq. ), as amended by section 3, is further amended by adding at the end the following:\n320D. Health care provider behavioral health and wellness programs (a) In general The Secretary may award grants to eligible entities for the purpose of establishing or enhancing behavioral health and wellness programs for health care providers. (b) Program description A behavioral health and wellness program funded under this section shall\u2014 (1) provide confidential support services for health care providers to help handle stressful or traumatic patient-related events, including counseling services and wellness seminars; (2) provide training to health care providers to serve as peer counselors to other health care providers; (3) purchase materials to be used exclusively to provide such training; and (4) disseminate such information and materials as are necessary to conduct such training and provide such peer counseling. (c) Definitions In this section, the term eligible entity means a hospital, including a critical access hospital (as defined in section 1861(mm)(1) of the Social Security Act) or a disproportionate share hospital (as defined in section 1923(a)(1)(A) of such Act), a Federally-qualified health center (as defined in section 1905(1)(2)(B) of such Act), or any other health care facility. .\n#### 5. Development of resources for educating mental health professionals about treating fire fighters and emergency medical services personnel\n##### (a) In general\nThe Administrator of the United States Fire Administration, in consultation with the Secretary of Health and Human Services, shall develop and make publicly available resources that may be used by the Federal Government and other entities to educate mental health professionals about\u2014\n**(1)**\nthe culture of Federal, State, Tribal, and local career, volunteer, and combination fire departments and emergency medical services agencies;\n**(2)**\nthe different stressors experienced by firefighters and emergency medical services personnel, supervisory firefighters and emergency medical services personnel, and chief officers of fire departments and emergency medical services agencies;\n**(3)**\nchallenges encountered by retired firefighters and emergency medical services personnel; and\n**(4)**\nevidence-based therapies for mental health issues common to firefighters and emergency medical services personnel within such departments and agencies.\n##### (b) Consultation\nIn developing resources under subsection (a), the Administrator of the United States Fire Administration and the Secretary of Health and Human Services shall consult with national fire and emergency medical services organizations.\n##### (c) Definitions\nIn this section:\n**(1) Chief officer**\nThe term chief officer means any individual who is responsible for the overall operation of a fire department or an emergency medical services agency, irrespective of whether such individual also serves as a firefighter or emergency medical services personnel.\n**(2) Emergency medical services personnel**\nThe term emergency medical services personnel means any employee, regardless of rank or whether the employee receives compensation, as defined in section 1204(7) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284(7) ).\n**(3) Firefighter**\nThe term firefighter means any employee, regardless of rank or whether the employee receives compensation, of a Federal, State, Tribal, or local fire department who is responsible for responding to calls for emergency service.\n#### 6. Best practices and other resources for addressing posttraumatic stress disorder in public safety officers\n##### (a) Development; updates\nThe Secretary of Health and Human Services shall\u2014\n**(1)**\ndevelop and assemble evidence-based best practices and other resources to identify, prevent, and treat posttraumatic stress disorder and co-occurring disorders in public safety officers; and\n**(2)**\nreassess and update, as the Secretary determines necessary, such best practices and resources, including based upon the options for interventions to reduce suicide among public safety officers identified in the annual reports required by section 317W(e)(1)(F) of the Public Health Service Act, as added by section 2 of this Act.\n##### (b) Consultation\nIn developing, assembling, and updating the best practices and resources under subsection (a), the Secretary of Health and Human Services shall consult with, at a minimum, the following:\n**(1)**\nPublic health experts.\n**(2)**\nMental health experts with experience in studying suicide and other profession-related traumatic stress.\n**(3)**\nClinicians with experience in diagnosing and treating mental health issues.\n**(4)**\nRelevant national police, fire, and emergency medical services organizations.\n##### (c) Availability\nThe Secretary of Health and Human Services shall make the best practices and resources under subsection (a) available to Federal, State, and local fire, law enforcement, and emergency medical services agencies.\n##### (d) Federal training and development programs\nThe Secretary of Health and Human Services shall work with Federal departments and agencies, including the United States Fire Administration, to incorporate education and training on the best practices and resources under subsection (a) into Federal training and development programs for public safety officers.\n##### (e) Definition\nIn this section, the term public safety officer means\u2014\n**(1)**\na public safety officer, as defined in section 1204 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 ); or\n**(2)**\na public safety telecommunicator, as described in detailed occupation 43\u20135031 in the Standard Occupational Classification Manual of the Office of Management and Budget (2018).",
      "versionDate": "2025-03-06",
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
        "updateDate": "2025-03-25T15:44:55Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1902ih.xml"
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
      "title": "HERO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HERO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Emergency Responders Overcome Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Health and Human Services to improve the detection, prevention, and treatment of mental health issues among public safety officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T05:33:20Z"
    }
  ]
}
```
