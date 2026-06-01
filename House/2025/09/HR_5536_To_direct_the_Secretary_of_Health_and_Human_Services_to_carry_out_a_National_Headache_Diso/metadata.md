# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5536?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5536
- Title: HEADACHE Act
- Congress: 119
- Bill type: HR
- Bill number: 5536
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2026-05-30T08:06:02Z
- Update date including text: 2026-05-30T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5536",
    "number": "5536",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000482",
        "district": "3",
        "firstName": "Lori",
        "fullName": "Rep. Trahan, Lori [D-MA-3]",
        "lastName": "Trahan",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "HEADACHE Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:02Z",
    "updateDateIncludingText": "2026-05-30T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:01:50Z",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "MA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-19",
      "state": "NC"
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
      "sponsorshipDate": "2025-09-26",
      "state": "PA"
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
      "sponsorshipDate": "2025-09-26",
      "state": "DC"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NJ"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NJ"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NY"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "OR"
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
      "sponsorshipDate": "2025-10-31",
      "state": "MA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "DE"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
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
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "IL"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "AL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MI"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-12-30",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MA"
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
      "sponsorshipDate": "2026-02-10",
      "state": "NC"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
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
      "sponsorshipDate": "2026-02-10",
      "state": "IN"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "MA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CT"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "NY"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NM"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "VA"
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
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "OR"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NY"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "VT"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "ME"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "WA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5536ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5536\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mrs. Trahan (for herself, Ms. Budzinski , Mr. Moulton , Ms. Kelly of Illinois , and Mrs. Foushee ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to carry out a National Headache Disorders Initiative, to establish an Advisory Council on Headache Disorders Research, Care, and Services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Headache Education, Access, Diagnosis, and Care Health Equity Act or the HEADACHE Act .\n#### 2. Definition\nIn this Act:\n**(1) Headache disorder**\n**(A) In general**\nThe term headache disorder means a primary or secondary medical condition for which headache is a principal symptom.\n**(B) Inclusion of certain medical conditions**\nThe medical conditions referred to in subparagraph (A) include migraine, cluster headache, tension-type headache, spinal cerebrospinal fluid (CSF) leak, idiopathic intracranial hypertension, new daily persistent headache, headache secondary to long COVID, orofacial pain disorders, post-traumatic headache secondary to traumatic brain injury, and headache disorders affecting vulnerable populations such as children, pregnant women, and older adults.\n**(2) Secretary**\nThe term Secretary means the Secretary of Health and Human Services, except as otherwise specifically provided.\n#### 3. National Headache Disorders Initiative\n##### (a) In general\nThe Secretary shall carry out an initiative, to be known as the National Headache Disorders Initiative (in this section referred to as the NHDI ), in accordance with the requirements of this section.\n##### (b) Components\nIn carrying out the NHDI, the Secretary shall\u2014\n**(1)**\nestablish and implement a comprehensive program to address the medical, societal, and economic impacts of headache disorders;\n**(2)**\ntake such actions as may be necessary to increase the clinical and research workforce focused on the care of patients with headache disorders;\n**(3)**\ncoordinate with other Federal initiatives with missions that overlap with NHDI, including the Helping End Addiction Long-Term (HEAL) Initiative, the NIH Pain Consortium, the Interagency Pain Research Coordinating Committee, and the Centers of Excellence in Pain Education;\n**(4)**\nensure that Federal resources available to support headache disorders research and services across all agencies are commensurate with the high disease burden exacted by these conditions;\n**(5)**\nensure prioritization of fundamental, translational, and clinical research to improve the speed, accuracy, and cost of diagnosis of headache disorders, and the development of innovative therapeutics to prevent and ameliorate the symptoms of headache disorders;\n**(6)**\nimprove protocols for the diagnosis and the coordination of care of headache disorders, including care pathways that address comorbid medical conditions;\n**(7)**\nenhance the epidemiological database of headache disorders to ensure comprehensive and inclusive data collection that improves clinical care, research, and public health efforts while addressing disparities in diagnosis, treatment, and access to care;\n**(8)**\nenhance social research of headache disorders and coordinate public awareness campaigns to reduce stigma associated with such disorders; and\n**(9)**\ncoordinate with international bodies to integrate and inform global efforts surrounding headache disorders.\n##### (c) Duties\nThe Secretary shall\u2014\n**(1)**\noversee the establishment and updating of the NHDI; and\n**(2)**\nevaluate all Federal programs related to headache disorders, including budget requests and approvals.\n#### 4. Advisory Council on Headache Disorders Research, Care, and Services\n##### (a) Establishment\nThe Secretary shall establish and maintain an Advisory Council on Headache Disorders Research, Care, and Services (referred to in this section as the Advisory Council ) for the purpose of advising the Secretary on matters relating to headache disorders.\n##### (b) Membership\n**(1) Federal members**\nThe Advisory Council shall be comprised of experts, to be appointed by the Secretary, who collectively are from various backgrounds and perspectives, including at least one member from each of the following:\n**(A)**\nThe National Institutes of Health.\n**(B)**\nThe Office of Research on Women\u2019s Health.\n**(C)**\nThe Food and Drug Administration.\n**(D)**\nThe Centers for Medicare & Medicaid Services.\n**(E)**\nThe Indian Health Service.\n**(F)**\nThe Department of Veterans Affairs.\n**(G)**\nThe Department of Defense.\n**(H)**\nThe Centers for Disease Control and Prevention.\n**(I)**\nThe Agency for Healthcare Research and Quality.\n**(J)**\nThe Patient-Centered Outcomes Research Institute.\n**(K)**\nThe Advanced Research Projects Agency for Health.\n**(L)**\nThe National Center for Complementary and Integrative Health.\n**(M)**\nThe Department of Education.\n**(N)**\nOther Federal departments and agencies.\n**(2) Non-Federal members**\nIn addition to the members specified in paragraph (1), the Advisory Council shall include 12 members, to be appointed by the Secretary, who shall include representatives of minority communities, communities disproportionately affected by headache disorders, and communities underrepresented in headache disorders research, who shall each be from outside the Federal Government, and who shall include the following:\n**(A)**\nTwo individuals who are patient advocates, including one individual who is living with migraine and one individual with a non-migraine headache disorder.\n**(B)**\nAn individual who is a caregiver of a child or adolescent with a headache disorder.\n**(C)**\nIndividuals who are healthcare providers specializing in headache (those with a patient base where greater than 80 percent are headache patients), including\u2014\n**(i)**\nat least one individual who is Doctor of Medicine or Doctor of Osteopathic Medicine;\n**(ii)**\nat least one individual who is an Advanced Practice Provider;\n**(iii)**\nat least one individual who is a behavioral health specialist;\n**(iv)**\nat least one individual who is an orofacial pain specialist;\n**(v)**\nat least one individual who is a front-line provider (such as a primary care physician or emergency care provider); and\n**(vi)**\nat least one individual who is a researcher with expertise in headache disorders.\n**(D)**\nAt least one individual who is a representative of a non-profit patient advocacy organization focused exclusively on headache disorders.\n##### (c) Meetings\n**(1) Frequency**\nThe Advisory Council shall meet\u2014\n**(A)**\nat least once each quarter during the 2-year period beginning on the date on which the Advisory Council is established; and\n**(B)**\nat the Secretary\u2019s discretion after the expiration of such period.\n**(2) Annual research meeting**\nNot later than two years after the date of enactment of this Act, and every year thereafter, the Advisory Council shall convene a meeting of Federal and non-Federal organizations to discuss headache disorders research.\n##### (d) Termination\nThe Advisory Council shall terminate on the sunset date specified in section 7.\n#### 5. Data sharing\n##### (a) In general\nThe heads of Federal agencies, within and outside the Department of Health and Human Services, that have data relating to headache disorders shall, at the request of the Secretary, share such data with the Secretary to enable the Secretary to complete the report required under section 6.\n##### (b) Included data\nThe data-sharing requirement under subsection (a) includes standardized data collection across agencies and integration with non-Federal sources, such as electronic health records, patient registries, and population health surveys.\n#### 6. Annual report to Congress\n##### (a) In general\nThe Secretary shall submit to Congress an annual report containing information relating to headache disorders, as specified in subsection (b).\n##### (b) Contents\nThe annual report shall include the following:\n**(1)**\nAn evaluation of all federally funded efforts relating to headache disorders research, clinical care, and other treatment programs and their outcomes.\n**(2)**\nAn evaluation of program performance, mission, and purpose, including data on headache disparities across racial, ethnic, socioeconomic, and geographic lines.\n**(3)**\nRecommendations for priority actions, including\u2014\n**(A)**\nreducing the financial impact of headache disorders on Medicare and other federally funded programs;\n**(B)**\nimproving health outcomes by updating diagnostic protocols, improving access to care, and advancing therapeutic research; and\n**(C)**\nstrategies to increase public awareness and reduce stigma.\n**(4)**\nAn annually updated national plan that addresses both short-term and long-term objectives for addressing headache disorders.\n#### 7. Sunset date\nThis Act shall cease to be effective on the date that is 5 years after the date of enactment of this Act.",
      "versionDate": "2025-09-19",
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
        "updateDate": "2025-12-15T20:09:23Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5536ih.xml"
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
      "title": "HEADACHE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-08T09:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEADACHE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-08T09:08:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Headache Education, Access, Diagnosis, and Care Health Equity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-08T09:08:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to carry out a National Headache Disorders Initiative, to establish an Advisory Council on Headache Disorders Research, Care, and Services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-08T09:03:12Z"
    }
  ]
}
```
