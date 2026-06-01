# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6601?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6601
- Title: CARE for First Responders Act
- Congress: 119
- Bill type: HR
- Bill number: 6601
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-04-16T08:07:13Z
- Update date including text: 2026-04-16T08:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6601",
    "number": "6601",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "CARE for First Responders Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:07:13Z",
    "updateDateIncludingText": "2026-04-16T08:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:34:02Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-10T15:05:35Z",
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
      "sponsorshipDate": "2025-12-10",
      "state": "PA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "VT"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NM"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "DC"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
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
      "sponsorshipDate": "2026-02-02",
      "state": "MN"
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
      "sponsorshipDate": "2026-02-09",
      "state": "OH"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "MI"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "RI"
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NJ"
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
      "sponsorshipDate": "2026-04-15",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6601ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6601\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Ms. Tokuda (for herself, Mr. Fitzpatrick , Ms. Balint , Mr. LaMalfa , and Mr. Tran ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo increase access to mental health, substance use, and counseling services for first responders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Crisis Assistance and Resources in Emergencies for First Responders Act or the CARE for First Responders Act .\n#### 2. Crisis counseling assistance and training\n##### (a) In general\nSection 416(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5183(a) ) is amended by inserting and to qualified emergency response providers responding to major disasters after victims of major disasters .\n##### (b) Definitions\nSection 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ) is amended by adding at the end the following:\n(13) Public safety telecommunicator The term public safety telecommunicator means a public safety telecommunicator as designated in detailed occupation 43\u20135031 in the Standard Occupational Classification Manual of the Office of Management and Budget issued in 2018, or any successor designation. (14) Qualified emergency response providers The term qualified emergency response providers means\u2014 (A) emergency response providers (as defined in section 2 of the Homeland Security Act of 2002 ( 6 U.S.C. 101 )); and (B) public safety telecommunicators. .\n#### 3. Specialized services for first responders\nSubpart 3 of part B of title V of the Public Health Service Act ( 42 U.S.C. 290bb\u201331 ) is amended by adding at the end the following:\n520O. Specialized services for first responders (a) Establishment Not later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Assistant Secretary of the Substance Abuse and Mental Health Administration, shall develop and carry out a comprehensive program designed to provide mental health services specifically tailored to qualified emergency response providers. Such program shall\u2014 (1) provide for mental health care availability to qualified emergency response providers on a 24-hour basis; (2) provide for a qualified emergency response providers hotline operated through the 988 Suicide and Crisis Lifeline under section 520E\u20133 of the Public Health Service Act ( 42 U.S.C. 290bb\u201336c ) that is confidential and toll-free, sufficiently staffed by appropriately trained mental health personnel and available at all times; and (3) provide for outreach to, and education programs for, qualified emergency response providers and their families, with priority given to qualified emergency response providers of major disasters. (b) Best practices research (1) In general The Secretary shall, in consultation with the heads of the agencies specified in paragraph (2), conduct or support research on best practices for providing mental health services to, and prevent suicide among, qualified emergency response providers. (2) Agencies specified The agencies specified in this paragraph are the following: (A) The Department of Homeland Security. (B) The Federal Emergency Management Agency. (C) The United States Fire Administration. (D) The National Institute of Mental Health. (E) The Centers for Disease Control and Prevention. (F) The Department of Justice. (c) Information addressed in education programs Education provided under subsection (a)(3) shall include information designed to\u2014 (1) remove the stigma associated with mental illness; (2) encourage qualified emergency response providers to seek treatment and assistance for mental illness; (3) promote skills for coping with mental illness; and (4) help families of qualified emergency response providers with\u2014 (A) understanding issues arising from the transition of qualified emergency response providers back into family life and regular work, following the end of a disaster assignment; (B) identifying signs and symptoms of mental illness; and (C) encouraging qualified emergency response providers to seek assistance for mental illness. (d) Peer support counseling program (1) In general The Secretary shall, as part of the comprehensive program under this section, establish and carry out a peer support counseling program, under which active and retired qualified emergency response providers may volunteer as peer counselors\u2014 (A) to assist other qualified emergency response providers with issues related to mental health, readiness, and readjustment; and (B) to conduct outreach to qualified emergency response providers and their families. (2) Administration In carrying out the peer support counseling program under this section, the Secretary shall\u2014 (A) provide for adequate training of individuals who volunteer to serve as peer counselors, including training carried out under section 416(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act; and (B) coordinate with such community organizations, State and local governments, institutions of higher education, chambers of commerce, local business organizations, organizations that provide mental health services, and other organizations as the Secretary considers appropriate. (e) Other components The Secretary may take such other actions to carry out the comprehensive program under this section as the Secretary determines appropriate for purposes of reducing the incidence of mental illness and suicide among qualified emergency response providers. (f) Definitions In this section: (1) Major disaster The term major disaster has the meaning given such term in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ). (2) Public safety telecommunicators The term public safety telecommunicator means a public safety telecommunicator as designated in detailed occupation 43\u20135031 in the Standard Occupational Classification Manual of the Office of Management and Budget issued in 2018, or any successor designation. (3) Qualified emergency response providers The term qualified emergency response providers means\u2014 (A) emergency response providers (as defined in section 2 of the Homeland Security Act of 2002 ( 6 U.S.C. 101 )); and (B) public safety telecommunicators. 520P. On-site mental health services grants (a) In general The Secretary, acting through the Assistant Secretary for Mental Health and Substance Use, shall award competitive grants to eligible entities to establish a new health care delivery site that is a mobile unit to provide integrated, short-term crisis services to qualified emergency response providers of a major disaster. Such services shall be\u2014 (1) linguistically and culturally appropriate; (2) trauma-informed; and (3) incorporate disaster behavioral interventions. (b) Use of funds An eligible entity that receives a grant under this subsection may use funds received through the grant to provide mobile crisis response, stabilization, and intervention services, including\u2014 (1) initial support and triage via mobile crisis team visits; (2) on-site screening and evaluation of mental and behavioral health issues; (3) assessment of current supports and resources; (4) short-term crisis management throughout a major disaster; (5) referral for appropriate follow-up services, including sub-acute or acute hospital care; (6) supportive, collaborative crisis planning; (7) consultation with existing supports and services; and (8) self-care techniques and resilience training. (c) Authorized purchase or lease The Secretary may purchase or lease equipment for purposes of carrying out this section, which may include data and information systems (including the costs of repaying the principal of, and paying the interest on, loans for equipment). (d) Grant terms (1) Maximum amount The amount of a grant awarded under subsection (a) may not exceed $150,000. (2) Duration The term of a grant awarded under subsection (a) shall be for a period of not less than 6 months. Such term is renewable for a single, additional term so that the total term of the grant does not exceed 2 years. (e) Evaluations and Technical Assistance The Secretary shall\u2014 (1) evaluate the activities supported by grants awarded under subsection (a), and disseminate, as appropriate, the findings from the evaluation; (2) provide appropriate information, training, and technical assistance, as appropriate, to eligible entities that receive a grant under this section, to help such entities to meet the requirements of this section, including assistance with selection and implementation of evidence-based interventions and frameworks to protect the mental health of qualified emergency response providers; and (3) identify best practices, as applicable, to improve the identification, assessment, treatment, and timely transition, as appropriate, to additional or follow-up care for qualified emergency response providers who are at risk for mental illness, suicide, and substance abuse, and enhance the coordination of care for such individuals during and after a major disaster, in support of activities supported by grants awarded under subsection (a). (f) Definitions (1) Eligible entity The term eligible entity means a State, local, territorial, or Tribal health department, community health center, rural health clinic, or nonprofit organization that\u2014 (A) is located in or around a major disaster area; and (B) has experience working with qualified mental health professionals in providing mental health, substance use, or counseling services. (2) Major disaster The term major disaster has the meaning given such term in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ). (3) Major disaster area The term major disaster area has the meaning given such term in section 625.2 of title 20, Code of Federal Regulations (or successor regulations). (4) Public safety telecommunicators The term public safety telecommunicator means a public safety telecommunicator as designated in detailed occupation 43\u20135031 in the Standard Occupational Classification Manual of the Office of Management and Budget issued in 2018, or any successor designation. (5) Qualified emergency response providers The term qualified emergency response providers means\u2014 (A) emergency response providers (as defined in section 2 of the Homeland Security Act of 2002 ( 6 U.S.C. 101 )); and (B) public safety telecommunicators. (6) Qualified mental health professional The term qualified mental health professional means a health care practitioner or social and human services provider who\u2014 (A) is licensed or certified under State law in the State involved; and (B) offers services for the purpose of improving an individual\u2019s mental health or to treat mental health or substance use disorders, including\u2014 (i) a physician, allopathic physicians, osteopathic physician, nurse practitioner, or physician assistant with a specialty in mental and psychiatry; (ii) a health service psychologist; (iii) a licensed clinical social worker; (iv) a psychiatric nurse specialist; (v) a marriage and family therapist; (vi) a licensed professional counselor; (vii) a substance use disorder counselor; (viii) an occupational therapist; or (ix) any other individual who\u2014 (I) has not yet been licensed or certified to serve as a professional listed in any of clauses (i) through (viii); and (II) will serve at a Federally qualified health center (as defined in section 1861(aa)(4) of the Social Security Act) under the supervision of a licensed individual or certified professional so listed. (g) Authorization of appropriations There is authorized to be appropriated to carry out this section $5,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-12-10",
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
        "updateDate": "2026-01-07T17:58:51Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6601ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase access to mental health, substance use, and counseling services for first responders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:26Z"
    },
    {
      "title": "CARE for First Responders Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CARE for First Responders Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Crisis Assistance and Resources in Emergencies for First Responders Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:21Z"
    }
  ]
}
```
