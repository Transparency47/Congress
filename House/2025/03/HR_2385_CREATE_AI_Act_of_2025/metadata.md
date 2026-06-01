# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2385?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2385
- Title: CREATE AI Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2385
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2026-05-21T20:39:30Z
- Update date including text: 2026-05-21T20:39:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2385",
    "number": "2385",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "CREATE AI Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T20:39:30Z",
    "updateDateIncludingText": "2026-05-21T20:39:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
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
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "VA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-01",
      "state": "PA"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "FL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "OR"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "DE"
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
      "sponsorshipDate": "2025-04-02",
      "state": "GA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "GA"
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
      "sponsorshipDate": "2025-04-17",
      "state": "MI"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "WA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "OR"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-11",
      "state": "VA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NC"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CO"
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
      "sponsorshipDate": "2025-11-17",
      "state": "NJ"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "FL"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MI"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "NM"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NV"
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
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2385ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2385\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Obernolte (for himself and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo establish the National Artificial Intelligence Research Resource, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Creating Resources for Every American To Experiment with Artificial Intelligence Act of 2025 or the CREATE AI Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCutting-edge artificial intelligence research relies on access to computational resources and large datasets.\n**(2)**\nAccess to the computational resources and datasets necessary for artificial intelligence research and development is often limited to very large technology companies.\n**(3)**\nThe lack of access to computational and data resources has resulted in insufficient diversity in the artificial intelligence research and development community.\n**(4)**\nEngaging the full and diverse talent of the United States is critical for maintaining United States leadership in artificial intelligence and ensuring that artificial intelligence is developed in a manner that benefits all people of the United States.\n**(5)**\nThe National Artificial Intelligence Research Resource Task Force, authorized under section 5106 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 et seq. ), recommended the establishment of a National Artificial Intelligence Research Resource in a report entitled Strengthening and Democratizing the U.S. Artificial Intelligence Innovation Ecosystem: An Implementation Plan for a National Artificial Intelligence Research Resource , issued on January 24, 2023.\n#### 3. National Artificial Intelligence Research Resource\n##### (a) NAIRR steering subcommittee\nSection 5103 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 9413 ) is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (f); and\n**(2)**\nby inserting after subsection (d) the following:\n(e) NAIRR Steering Subcommittee (1) Definition In this subsection, the terms NAIRR , National Artificial Intelligence Research Resource , Operating Entity , Program Management Office , and resources of the NAIRR have the meanings given the terms in section 5601. (2) Establishment There is established within the Interagency Committee a Steering Subcommittee for the National Artificial Intelligence Research Resource (referred to in this section as the NAIRR Steering Subcommittee ). (3) Chair and assistant chairs The NAIRR Steering Subcommittee shall be chaired by the Director of the Office of Science and Technology Policy. The Director of the Office of Science and Technology Policy may establish assistant chairs of the NAIRR Steering Subcommittee based on members of the NAIRR Steering Subcommittee rotating into the assistant chair positions on a predetermined schedule. (4) Membership The Director of the Office of Science and Technology Policy shall select members of the Interagency Committee to serve on the NAIRR Steering Subcommittee that the Director determines\u2014 (A) have substantial expertise; (B) have substantially funded or conducted artificial intelligence research and development; or (C) have some other significant relationship with the NAIRR. (5) Changes to NAIRR Steering Subcommittee composition Not less frequently than once a year, the Director of the Office of Science and Technology Policy shall review the composition of the NAIRR Steering Subcommittee and update such composition, which may include adding or removing members from the NAIRR Steering Subcommittee, if necessary. (6) Subcommittees and working groups The NAIRR Steering Subcommittee may establish subcommittees, working groups, or other permanent or temporary bodies of certain members of the NAIRR Steering Subcommittee. (7) Duties The NAIRR Steering Subcommittee shall\u2014 (A) coordinate with the National Science Foundation and the Program Management Office to\u2014 (i) oversee and approve the operating plan for the NAIRR; (ii) review the budget for the NAIRR; (iii) develop and release a request for proposals to solicit bids for the Operating Entity, including establishing the terms and conditions and functions of the Operating Entity; and (iv) develop and release funding opportunities for resources of the NAIRR; (B) work with the Program Management Office to establish criteria for the Operating Entity, review candidates, and select an entity to act as the Operating Entity; (C) identify resources that could be federated, participate in resource provider selection and funding, and provide direction to the Operating Entity about resource allocation and how those resources should be made accessible via the NAIRR; (D) define key performance indicators for the NAIRR, in conjunction with the Program Management Office and any relevant Advisory Committees established under section 5602(c); (E) evaluate NAIRR performance against the key performance indicators defined under subparagraph (D) on a periodic basis and not less frequently than once every year; (F) develop an annual report, transmitted to the Director of the Office of Science and Technology Policy and publicly released, on the progress of the National Artificial Intelligence Research Resource that includes\u2014 (i) a summary of the results of the evaluation conducted under subparagraph (E); and (ii) any recommendations for changes to the NAIRR; and (G) oversee a periodic independent assessment of the NAIRR. (8) Provision of resources of the NAIRR Each agency comprising the NAIRR Steering Subcommittee is authorized to provide the Operating Entity with resources of the NAIRR or funding for resources of the NAIRR. .\n##### (b) In general\nThe National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 et seq. ) is amended by adding at the end the following:\nLVI National Artificial Intelligence Research Resource Sec. 5601. Definitions. Sec. 5602. Establishment; governance. Sec. 5603. Resources of the NAIRR. Sec. 5604. NAIRR processes and procedures. Sec. 5605. NAIRR funding. 5601. Definitions In this title: (1) Advisory Committee The term Advisory Committee means any Advisory Committee established under section 5602(c). (2) AI testbed The term AI testbed means a testbed described in section 22A(g) of the National Institute of Standards and Technology Act ( 15 U.S.C. 278h\u20131(g) ). (3) Executive agency The term Executive agency has the meaning given such term in section 105 of title 5, United States Code. (4) National Artificial Intelligence Research Resource; NAIRR The terms National Artificial Intelligence Research Resource and NAIRR have the meaning given the term National Artificial Intelligence Research Resource in section 5601(g). (5) Operating Entity The term Operating Entity means the Operating Entity selected by the Program Management Office as described in section 5602(b)(3)(A). (6) Program Management Office The term Program Management Office means the Program Management Office established under section 5602(b). (7) Resource of the NAIRR The term resource of the NAIRR means a resource described in section 5603(b). (8) NAIRR Steering Subcommittee The term NAIRR Steering Subcommittee means the NAIRR Steering Subcommittee established under section 5103(e). (9) STEM The term STEM means science, technology, engineering, and mathematics, including computer science. 5602. Establishment; governance (a) Establishment Not later than one year after the date of the enactment of the Creating Resources for Every American To Experiment with Artificial Intelligence Act of 2025 , the Director of the National Science Foundation, in coordination with the NAIRR Steering Subcommittee, shall establish the National Artificial Intelligence Research Resource to\u2014 (1) spur innovation and advance the development of artificial intelligence to stimulate cutting-edge research and propel the strategic development of artificial intelligence capabilities; (2) improve access to artificial intelligence resources for researchers and students of artificial intelligence; (3) improve capacity for artificial intelligence research in the United States; and (4) support the testing, benchmarking, and evaluation of artificial intelligence systems developed and deployed in the United States. (b) Program Management Office (1) Establishment The Director of the National Science Foundation shall establish within the National Science Foundation a Program Management Office to oversee the day-to-day functions of the NAIRR and shall appoint an individual to head the Program Management Office. (2) Staff (A) In general The head of the Program Management Office may identify staff and direct all employees of the Program Management Office, in accordance with the applicable provisions of title 5, United States Code. (B) Representation and requirements The staff of the Program Management Office\u2014 (i) may include representation from other Federal agencies providing support for NAIRR resources; and (ii) shall include not fewer than three full-time employees. (3) Duties The duties of the Program Management Office shall include\u2014 (A) in coordination with the NAIRR Steering Subcommittee and any relevant Advisory Committee as appropriate\u2014 (i) developing the funding opportunity and soliciting bids for the Operating Entity, which will be responsible for operation of the National Artificial Intelligence Research Resource; (ii) selecting, through a competitive and transparent process, a nongovernmental organization, which may be an independent legal entity or a consortium of 1 or more partners (which may include federally funded research and development centers), to be designated the Operating Entity; (iii) overseeing compliance with the contractual obligations of the Operating Entity; (iv) establishing evaluation criteria for the NAIRR; (v) overseeing asset allocation and utilization; (vi) identifying an external independent evaluation entity; (vii) assessing the performance of the Operating Entity on not less than an annual basis and, if such performance is unsatisfactory, ending the agreement with such Operating Entity and selecting a new Operating Entity in accordance with clause (ii); (viii) developing multi-agency funding opportunities for the selection of NAIRR resources; and (ix) coordinating resource contributions from participating Federal agencies; and (B) delegating, with appropriate oversight, operational tasks to the Operating Entity, including\u2014 (i) coordinating the provisioning of resources of the NAIRR; (ii) maintaining a portal and associated services for users to access resources of the NAIRR; (iii) developing policies and procedures for the NAIRR; (iv) hiring and managing a staff (including experts in cyber infrastructure management, data science, research design, privacy, ethics, and legal and policy matters) to support the operations of the NAIRR; (v) continually modernizing NAIRR infrastructure; (vi) recommending key performance indicators for the NAIRR, in coordination with the NAIRR Steering Subcommittee and any relevant Advisory Committee; (vii) publishing publicly available annual reports reviewing the performance of the NAIRR, the resources of the NAIRR, and the NAIRR governance structures; (viii) establishing and administering training to new users on accessing a resource of the NAIRR, research design, and issues related to privacy, ethics, safety, and trustworthiness of artificial intelligence systems; (ix) facilitating connections to AI testbeds; and (x) making educational resources of the NAIRR available to other Federal agencies, and to Congress, for the purpose of educating Federal Government officials and employees about artificial intelligence. (c) Advisory Committees The head of the Program Management Office, acting through the Director of the Operating Entity, shall establish Advisory Committees to provide advice to the Operating Entity and the Program Management Office. Any such Advisory Committees shall be comprised of members from government agencies, the private sector, academia, and public interest groups. Chapter 10 of title 5, United States Code, shall not apply to any such Advisory Committee. 5603. Resources of the NAIRR (a) In general The head of the Program Management Office, acting through the Director of the Operating Entity and in coordination with the NAIRR Steering Subcommittee and any relevant Advisory Committee, shall\u2014 (1) coordinate and provision resources of the NAIRR; (2) establish processes to manage the procurement of new resources of the NAIRR, and intake of in-kind contribution of resources of the NAIRR, from Federal agencies or other entities; (3) establish policies on and review resources of the NAIRR for concerns related to ethics and privacy; (4) retire resources of the NAIRR no longer available or needed; and (5) publicly report a summary of categories of available resources of the NAIRR, categories of sources of such resources of the NAIRR, and issues related to resources of the NAIRR. (b) Resources of the NAIRR The NAIRR shall offer resources that include, at a minimum, all of the following, subject to the availability of appropriations: (1) A mix of computational resources, including\u2014 (A) on-premises, cloud-based, hybrid, and emergent resources; (B) public cloud providers providing access to popular computational and storage services for NAIRR users; (C) an open source software environment for the NAIRR; (D) an application programming interface providing structured access to artificial intelligence models; and (E) other types of computational resources. (2) Data, including by\u2014 (A) (i) in coordination with the National Institute of Standards and Technology and consistent with the guidance of the National Science and Technology Council titled Desirable Characteristics of Data Repositories for Federally Funded Data, dated May 2022, or any successor document, publishing interoperability standards for data repositories based on the data sharing and documentation standards and guidelines produced under section 22A of the National Institute of Standards and Technology Act ( 15 U.S.C. 278h\u20131 ); and (ii) selecting and developing, through a competitive bidding process, data repositories to be available to NAIRR users; (B) establishing acceptable criteria for datasets used as resources of the NAIRR; (C) identifying and providing access to existing curated datasets of value and interest to the NAIRR user community; (D) establishing an artificial intelligence open data commons to facilitate community sharing and curation of data, code, and models; (E) coordinating with the Interagency Council on Statistical Policy to explore options to make Federal statistical data available to NAIRR users, including through the standard application process established under section 3583(a) of title 44, United States Code; and (F) other types of computational resources. (3) Educational tools and services, including by\u2014 (A) facilitating and curating educational and training materials; (B) providing technical training and user support; and (C) providing targeted outreach and programming strategies to increase participation in STEM fields. (4) AI testbeds, including by\u2014 (A) in coordination with the National Institute of Standards and Technology, facilitating access to artificial intelligence testbeds through which researchers can measure, benchmark, test, or evaluate engineering or algorithmic developments; and (B) developing a comprehensive catalog of open AI testbeds. 5604. NAIRR processes and procedures (a) User eligibility (1) Eligible users Subject to paragraph (3), the following users shall be eligible for access to the NAIRR: (A) A researcher, educator, or student based in the United States that is affiliated with an entity described in paragraph (2). (B) An employee of an entity described in clause (iii) or (iv) of paragraph (2)(B) with a demonstrable mission-need. (2) Entities described An entity described in this paragraph is an entity that satisfies the following: (A) Is based in the United States. (B) Is one of the following: (i) An institution of higher education. (ii) A nonprofit institution (as such term is defined in section 4 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3703 )). (iii) An Executive agency. (iv) A federally funded research and development center. (v) A small business concern (as such term is defined in section 3 of the Small Business Act ( 15 U.S.C. 632 ), notwithstanding section 121.103 of title 13, Code of Federal Regulations) that has received funding from an Executive agency, including through the Small Business Innovation Research Program or the Small Business Technology Transfer Program (as described in section 9 of the Small Business Act ( 15 U.S.C. 638 )). (vi) A category of entity that the Director of the National Science Foundation and the Director of the Office of Science and Technology Policy, after consultation with the NAIRR Steering Subcommittee and any relevant Advisory Committee, determine shall be eligible. (vii) A consortium composed of entities described in clauses (i) through (vi). (3) Excluded entities (A) In general No individual is authorized to be an eligible user under paragraph (1) if the individual is employed by a foreign country that is listed in section 4872(d)(2) of title 10, United States Code, or is otherwise authorized by such country to act for or on its behalf. (B) Enforcement The Director of the National Science Foundation shall ensure that individuals authorized as eligible users meet the requirements of subparagraph (A). (b) Privacy, ethics, civil rights and civil liberties, safety, and trustworthiness (1) In general (A) Requirements The head of the Program Management Office, acting through the Director of the Operating Entity and in consultation with any relevant Advisory Committee, shall establish requirements, a review process for applications, and a process for auditing resources of the NAIRR and research conducted using resources of the NAIRR on matters related to privacy, ethics, safety, security, and trustworthiness of artificial intelligence systems developed using resources of the NAIRR. (B) Federal statistical data Any auditing process required under subparagraph (A) for Federal statistical data included in a resource of the NAIRR shall be completed by the head of a designated statistical agency (as defined in section 3576(e) of title 44, United States Code), in coordination with the Chief Statistician of the United States, consistent with relevant law. (2) Consistency The head of the Program Management Office shall ensure the requirements and processes described in paragraph (1) are consistent with the policies of the Office of Management and Budget policy and relevant policies of other Executive agencies. The head of the Program Management Office shall coordinate with the Senior Agency Official for Privacy and the General Counsel of the National Science Foundation in ensuring compliance with applicable privacy law and policy and Federal laws and regulations. (3) Availability The head of the Program Management Office, acting through the Director of the Operating Entity, shall\u2014 (A) when determining access to computational resources of the NAIRR, take into consideration the extent to which the access relates to privacy, ethics, safety, security, risk mitigation, and trustworthiness of artificial intelligence systems, or other topics that demonstrate that a project is in the public interest; (B) ensure that a significant percentage of the annual allotment of computational resources of the NAIRR is provided to projects the primary focus of which is related to any of the topics described in subparagraph (A); and (C) to the extent that demand for access to computational resources of the NAIRR exceeds availability, consider, on a priority basis, projects focusing on any of the topics described in subparagraph (A) when ranking applications for such access. (c) Scientific integrity (1) In general The head of the Program Management Office, acting through the Director of the Operating Entity and in consultation with any relevant Advisory Committee, shall develop guidance for\u2014 (A) addressing concerns related to matters of scientific integrity, including matters related to the effects or impacts of research and potential research enabled by the NAIRR; and (B) mechanisms for an employee of the Operating Entity, an employee of the Program Management Office, a member of the NAIRR Steering Subcommittee or an Advisory Committee, a researcher or student affiliated with a NAIRR user described in subsection (a)(1), an employee of a provider of a resource of the NAIRR, an employee of a NAIRR funding agency, or a member of the public to report violations of the guidance developed under this paragraph, including by confidential and anonymous means. (2) Consistency with government policies on scientific integrity The guidance developed under paragraph (1)(A) shall be published in a publicly accessible location on the website of the NAIRR. Such policies shall, to the degree practicable, be consistent with\u2014 (A) the Presidential memorandum entitled Restoring Trust in Government Through Scientific Integrity and Evidence-Based Policymaking , dated January 27, 2021, or successor document; and (B) reports produced pursuant to such Presidential memorandum (including the reports entitled Protecting the Integrity of Government Science , dated January 2022, and A Framework for Federal Scientific Integrity Policy and Practice , dated January 2023, published by the National Science and Technology Council, or successor documents). (d) System security and user access controls The head of the Program Management Office, acting through the Director of the Operating Entity and in consultation with the NAIRR Steering Subcommittee, the Director of the Office of Management and Budget, the Director of the National Institute of Standards and Technology, and the Director of the Cybersecurity and Infrastructure Security Agency\u2014 (1) shall establish minimum security requirements for all persons interacting with the NAIRR, consistent with the most recent version of the Cybersecurity Framework, or successor document, maintained by the National Institute of Standards and Technology; and (2) may establish tiers of security requirements and user access controls beyond the minimum requirements relative to security risks. (e) Fee schedule The head of the Program Management Office, acting through the Director of the Operating Entity, may establish a fee schedule for access to the NAIRR. Fees charged under this subsection may be retained and used for the purposes of this title. The Operating Entity may only charge fees in such fee schedule. Such fee schedule\u2014 (1) may differ by type of eligible user and type of affiliated entity described in subsection (a); (2) shall include a free tier of access based on appropriated funds and anticipated costs and demand; (3) may include cost-based charges for eligible users to purchase resources of the NAIRR beyond the resources included in a free or subsidized tier; and (4) shall ensure that the primary purpose of the NAIRR is to support research. (f) Research security The head of the Program Management Office, acting through the Director of the Operating Entity and in consultation with the NAIRR Steering Subcommittee and the Director of the Office of Science and Technology Policy, shall\u2014 (1) ensure conformance with the requirements of National Security Presidential Memorandum\u201333 (relating to supported research and development national policy), issued January 2021, and its implementation guidance on research security and research integrity, or any successor policy document or guidance, by establishing NAIRR operating principles that emphasize the research integrity principles of openness, reciprocity, and transparency; and (2) designate a member of the leadership team for the Operating Entity as a research security point of contact with responsibility for overseeing conformance with the National Security Presidential Memorandum\u201333 and its implementation guidance, or any successor policy document or guidance. 5605. NAIRR funding To carry out this title, to the maximum extent practicable, the NAIRR is authorized to accept and use donations of cash, services, and personal property from the private sector. .\n##### (c) Conforming amendments\nThe table of contents in section 2(b) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 134 Stat. 3388) is amended by inserting after the items relating to title LV the following:\nTitle LVI\u2014National Artificial Intelligence Research Resource Sec. 5601. Definitions. Sec. 5602. Establishment; governance. Sec. 5603. Resources of the NAIRR. Sec. 5604. NAIRR processes and procedures. Sec. 5605. NAIRR funding. .",
      "versionDate": "2025-03-26",
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
        "actionDate": "2026-04-27",
        "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committees on Energy and Commerce, Agriculture, Oversight and Government Reform, Education and Workforce, the Judiciary, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8516",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Leadership in AI Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-04-06T12:56:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-26",
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
          "measure-id": "id119hr2385",
          "measure-number": "2385",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-26",
          "originChamber": "HOUSE",
          "update-date": "2026-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2385v00",
            "update-date": "2026-02-13"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Creating Resources for Every American To Experiment with Artificial Intelligence Act of 2025 or the CREATE AI Act of 2025</strong></p><p>This bill establishes a national program to provide U.S. researchers, educators, and students with access to artificial intelligence (AI) data, computational resources, educational tools and services, and testbeds.</p><p>The program, to be known as the National Artificial Intelligence Research Resource (NAIRR), must be established by the National Science Foundation (NSF) to improve U.S. AI research capacity and spur the strategic development of AI capabilities. NAIRR may accept and use donated resources from the private sector and federal agencies.</p><p>Those eligible to use NAIRR resources are (1) researchers, educators, and students based in the United States and affiliated with a U.S. institution of higher education, nonprofit, executive agency, or other specified entity; and (2) employees of U.S. executive agencies or federally funded research and development centers with a demonstrable mission need.</p><p>NSF must select a nongovernmental organization to operate NAIRR (i.e., an <em>operating entity</em>) through a competitive and transparent process. The operating entity must ensure that a significant percentage of the annual allotment of computational resources is provided to projects primarily focused on AI privacy, ethics, safety, security, risk mitigation, or trustworthiness. The operating entity must also establish minimum security requirements for all individuals interacting with NAIRR.</p><p>The operating entity may establish a fee schedule for access to NAIRR, which must include a free tier of access and must ensure that the primary purpose of NAIRR is to support research.</p>"
        },
        "title": "CREATE AI Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2385.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating Resources for Every American To Experiment with Artificial Intelligence Act of 2025 or the CREATE AI Act of 2025</strong></p><p>This bill establishes a national program to provide U.S. researchers, educators, and students with access to artificial intelligence (AI) data, computational resources, educational tools and services, and testbeds.</p><p>The program, to be known as the National Artificial Intelligence Research Resource (NAIRR), must be established by the National Science Foundation (NSF) to improve U.S. AI research capacity and spur the strategic development of AI capabilities. NAIRR may accept and use donated resources from the private sector and federal agencies.</p><p>Those eligible to use NAIRR resources are (1) researchers, educators, and students based in the United States and affiliated with a U.S. institution of higher education, nonprofit, executive agency, or other specified entity; and (2) employees of U.S. executive agencies or federally funded research and development centers with a demonstrable mission need.</p><p>NSF must select a nongovernmental organization to operate NAIRR (i.e., an <em>operating entity</em>) through a competitive and transparent process. The operating entity must ensure that a significant percentage of the annual allotment of computational resources is provided to projects primarily focused on AI privacy, ethics, safety, security, risk mitigation, or trustworthiness. The operating entity must also establish minimum security requirements for all individuals interacting with NAIRR.</p><p>The operating entity may establish a fee schedule for access to NAIRR, which must include a free tier of access and must ensure that the primary purpose of NAIRR is to support research.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr2385"
    },
    "title": "CREATE AI Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating Resources for Every American To Experiment with Artificial Intelligence Act of 2025 or the CREATE AI Act of 2025</strong></p><p>This bill establishes a national program to provide U.S. researchers, educators, and students with access to artificial intelligence (AI) data, computational resources, educational tools and services, and testbeds.</p><p>The program, to be known as the National Artificial Intelligence Research Resource (NAIRR), must be established by the National Science Foundation (NSF) to improve U.S. AI research capacity and spur the strategic development of AI capabilities. NAIRR may accept and use donated resources from the private sector and federal agencies.</p><p>Those eligible to use NAIRR resources are (1) researchers, educators, and students based in the United States and affiliated with a U.S. institution of higher education, nonprofit, executive agency, or other specified entity; and (2) employees of U.S. executive agencies or federally funded research and development centers with a demonstrable mission need.</p><p>NSF must select a nongovernmental organization to operate NAIRR (i.e., an <em>operating entity</em>) through a competitive and transparent process. The operating entity must ensure that a significant percentage of the annual allotment of computational resources is provided to projects primarily focused on AI privacy, ethics, safety, security, risk mitigation, or trustworthiness. The operating entity must also establish minimum security requirements for all individuals interacting with NAIRR.</p><p>The operating entity may establish a fee schedule for access to NAIRR, which must include a free tier of access and must ensure that the primary purpose of NAIRR is to support research.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr2385"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2385ih.xml"
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
      "title": "CREATE AI Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CREATE AI Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Creating Resources for Every American To Experiment with Artificial Intelligence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the National Artificial Intelligence Research Resource, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:59Z"
    }
  ]
}
```
