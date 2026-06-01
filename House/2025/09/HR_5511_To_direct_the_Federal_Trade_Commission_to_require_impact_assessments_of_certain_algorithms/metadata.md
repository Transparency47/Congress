# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5511?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5511
- Title: Algorithmic Accountability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5511
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2026-04-30T08:06:45Z
- Update date including text: 2026-04-30T08:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5511",
    "number": "5511",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001067",
        "district": "9",
        "firstName": "Yvette",
        "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
        "lastName": "Clarke",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Algorithmic Accountability Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:45Z",
    "updateDateIncludingText": "2026-04-30T08:06:45Z"
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
          "date": "2025-09-19T13:02:05Z",
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
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "VT"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "MO"
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
      "sponsorshipDate": "2025-09-19",
      "state": "OH"
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
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "PA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "AL"
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
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-19",
      "state": "DC"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "WA"
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
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "PA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "MI"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-19",
      "state": "FL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "TN"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MA"
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
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MN"
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
      "sponsorshipDate": "2026-04-29",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5511ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5511\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Ms. Clarke of New York (for herself, Ms. Balint , Ms. Barrag\u00e1n , Mr. Bell , Ms. Brown , Mr. Davis of Illinois , Mr. Deluzio , Mr. Evans of Pennsylvania , Mr. Figures , Mrs. Foushee , Mr. Garc\u00eda of Illinois , Ms. Norton , Mr. Huffman , Mr. Jackson of Illinois , Ms. Jacobs , Ms. Jayapal , Ms. Kelly of Illinois , Ms. Lee of Pennsylvania , Mrs. Ramirez , Ms. Tlaib , Mr. Veasey , and Ms. Wilson of Florida ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Federal Trade Commission to require impact assessments of certain algorithms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Algorithmic Accountability Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Biometrics**\nThe term biometrics means any information that represents a biological, physiological, or behavioral attribute or feature of a consumer.\n**(2) Chair**\nThe term Chair means the Chair of the Commission.\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Consumer**\nThe term consumer means an individual.\n**(5) Covered algorithm**\nThe term covered algorithm means a computational process derived from machine learning, natural language processing, artificial intelligence techniques, or other computational processing techniques of similar or greater complexity, that, with respect to a consequential action\u2014\n**(A)**\ncreates or facilitates the creation of a product or information;\n**(B)**\npromotes, recommends, ranks, or otherwise affects the display or delivery of information that is material to the consequential action;\n**(C)**\nmakes a decision; or\n**(D)**\nfacilitates human decision making.\n**(6) Covered entity**\n**(A) In general**\nThe term covered entity means any person, partnership, or corporation over which the Commission has jurisdiction under section 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(2) )\u2014\n**(i)**\nthat deploys any covered algorithm;\n**(I)**\nhad greater than $50,000,000 in average annual gross receipts or is deemed to have greater than $250,000,000 in equity value for the 3-taxable-year period (or for the period during which the person, partnership, or corporation has been in existence, if such period is less than 3 years) preceding the most recent fiscal year, as determined in accordance with paragraphs (2) and (3) of section 448(c) of the Internal Revenue Code of 1986;\n**(II)**\npossesses, manages, modifies, handles, analyzes, controls, or otherwise uses identifying information about more than 1,000,000 consumers, households, or consumer devices for the purpose of developing or deploying any covered algorithm; or\n**(III)**\nis substantially owned, operated, or controlled by a person, partnership, or corporation that meets the requirements under subclause (I) or (II);\n**(ii)**\nthat\u2014\n**(I)**\nhad greater than $5,000,000 in average annual gross receipts or is deemed to have greater than $25,000,000 in equity value for the 3-taxable-year period (or for the period during which the person, partnership, or corporation has been in existence, if such period is less than 3 years) preceding the most recent fiscal year, as determined in accordance with paragraphs (2) and (3) of section 448(c) of the Internal Revenue Code of 1986; and\n**(II)**\ndeploys any covered algorithm that is developed for implementation or use, or that the person, partnership, or corporation reasonably expects to be implemented or used by any person, partnership, or corporation if such person, partnership, or corporation meets the requirements described in clause (i); or\n**(iii)**\nthat met the criteria described in clause (i) or (ii) within the previous 3 years.\n**(B) Inflation adjustment**\nFor purposes of applying this paragraph in any fiscal year after the first fiscal year that begins on or after the date of enactment of this Act, each of the dollar amounts specified in subparagraph (A) shall be increased by the percentage increase (if any) in the consumer price index for all urban consumers (U.S. city average) from such first fiscal year that begins after such date of enactment to the fiscal year involved.\n**(7) Critical decision**\nThe term critical decision means a decision or judgment that has any legal, material, or similarly significant effect on a consumer's life relating to access to or the cost, terms, or availability of\u2014\n**(A)**\neducation and vocational training, including assessment, accreditation, or certification;\n**(B)**\nemployment, workers management, or self-employment;\n**(C)**\nessential utilities, such as electricity, heat, water, internet or telecommunications access, or transportation;\n**(D)**\nfamily planning, including adoption services or reproductive services;\n**(E)**\nfinancial services, including any financial service provided by a mortgage company, mortgage broker, or creditor;\n**(F)**\nhealthcare, including mental healthcare, dental, or vision;\n**(G)**\nhousing or lodging, including any rental or short-term housing or lodging;\n**(H)**\nlegal services, including private arbitration or mediation; or\n**(I)**\nany other service, program, or opportunity decisions about which have a comparably legal, material, or similarly significant effect on a consumer's life as determined by the Commission through rulemaking.\n**(8) Deploy**\nThe term deploy means to implement, use, or make available for sale, license, or other commercial relationship.\n**(9) Develop**\nThe term develop means to design, code, produce, customize, or otherwise create or modify.\n**(10) Identifying information**\nThe term identifying information means any information, regardless of how the information is collected, inferred, predicted, or obtained that identifies or represents a consumer, household, or consumer device through data elements or attributes, such as name, postal address, telephone number, biometrics, email address, internet protocol address, social security number, or any other identifying number, identifier, or code.\n**(11) Impact assessment**\nThe term impact assessment means the ongoing study and evaluation of a covered algorithm and its impact on consumers.\n**(12) State**\nThe term State means each of the 50 States, the District of Columbia, and any territory or possession of the United States.\n**(13) Summary report**\nThe term summary report means documentation of a subset of information required to be addressed by the impact assessment as described in this Act or determined appropriate by the Commission.\n**(14) Third-party decision recipient**\nThe term third-party decision recipient means any person, partnership, or corporation (beyond the consumer and the covered entity) that receives a copy of or has access to the results of any decision or judgment that results from a covered entity's deployment of a covered algorithm.\n#### 3. Assessing the impact of covered algorithms\n##### (a) Acts prohibited\n**(1) In general**\nIt is unlawful for\u2014\n**(A)**\nany covered entity to violate a regulation promulgated under subsection (b); or\n**(B)**\nany person to knowingly provide substantial assistance to any covered entity in violating subsection (b).\n**(2) Preemption of private contracts**\nIt shall be unlawful for any covered entity to commit the acts prohibited in paragraph (1), regardless of specific agreements between entities or consumers.\n##### (b) Regulations\n**(1) In general**\nSubject to paragraph (2), not later than 2 years after the date of enactment of this Act, the Commission shall, in consultation with the Director of the National Institute of Standards and Technology, the Director of the National Artificial Intelligence Initiative, the Director of the Office of Science and Technology Policy, and other relevant stakeholders, including standards bodies, private industry, academia, technology experts, and advocates for civil rights, consumers, and impacted communities, promulgate regulations, in accordance with section 553 of title 5, United States Code, that\u2014\n**(A)**\nrequire each covered entity to perform impact assessment of any covered algorithm\u2014\n**(i)**\nthat was developed for implementation or use, or that the covered entity reasonably expects to be implemented or used, by any person, partnership, or corporation that meets the requirements described in section 2(6)(A)(i); and\n**(ii)**\nboth prior to and after deployment by the covered entity;\n**(B)**\nrequire each covered entity to maintain documentation of any impact assessment performed under subparagraph (A), including the applicable information described in section 4(a) for 3 years longer than the duration of time for which the covered algorithm is deployed;\n**(C)**\nrequire each person, partnership, or corporation that meets the requirements described in section 2(6)(A)(i) to disclose their status as a covered entity to any person, partnership, or corporation that sells, licenses, or otherwise provides through a commercial relationship any covered algorithm deployed by the covered entity;\n**(D)**\nrequire each covered entity to submit to the Commission, on an annual basis, a summary report for ongoing impact assessment of any deployed covered algorithm;\n**(E)**\nrequire each covered entity to submit an initial summary report to the Commission for any new covered algorithm prior to its deployment by the covered entity;\n**(F)**\nallow any person, partnership, or corporation over which the Commission has jurisdiction under section 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(2) ) that deploys any covered algorithm, but is not a covered entity, to submit to the Commission a summary report for any impact assessment performed with respect to such algorithm;\n**(G)**\nrequire each covered entity, in performing the impact assessment described in subparagraph (A), to the extent possible, to meaningfully consult (including through participatory design, independent auditing, or soliciting or incorporating feedback) with relevant internal stakeholders (such as employees, ethics teams, and responsible technology teams) and independent external stakeholders (such as representatives of and advocates for impacted groups, civil society and advocates, and technology experts) as frequently as necessary;\n**(H)**\nrequire each covered entity to attempt to eliminate or mitigate, in a timely manner, any impact made by a covered algorithm that demonstrates a likely material negative impact that has legal or similarly significant effects on a consumer's life;\n**(I)**\nestablish definitions for\u2014\n**(i)**\nwhat constitutes access to or the cost, terms, or availability of with respect to a critical decision;\n**(ii)**\nwhat constitutes possession , management , modification , and control with respect to identifying information;\n**(iii)**\nthe different categories of third-party decision recipients that a covered entity must document under section 5(1)(H); and\n**(iv)**\nany of the services, programs, or opportunities described in subparagraphs (A) through (I) of section 2(7) for the purpose of informing consumers, covered entities, and regulators, as the Commission deems necessary;\n**(J)**\nestablish guidelines for any person, partnership, or corporation to calculate the number of consumers, households, or consumer devices for which the person, partnership, or corporation possesses, manages, modifies, or controls identifying information for the purpose of determining covered entity status;\n**(K)**\nestablish guidelines for a covered entity to prioritize different covered algorithms deployed by the covered entity for performing impact assessment; and\n**(L)**\nestablish a required format for any summary report, as described in subparagraphs (D), (E), and (F), to ensure that such reports are submitted in an accessible and machine-readable format.\n**(2) Considerations**\nIn promulgating the regulations under paragraph (1), the Commission\u2014\n**(A)**\nshall take into consideration\u2014\n**(i)**\nthat certain assessment or documentation of a covered algorithm may only be possible at particular stages of the development and deployment of such algorithm or may be limited or not possible based on the availability of certain types of information or data or the nature of the relationship between the covered entity and consumers;\n**(ii)**\nthe duration of time between summary report submissions and the timeliness of the reported information;\n**(iii)**\nthe administrative burden placed on the Commission and the covered entity;\n**(iv)**\nthe benefits of standardizing and structuring summary reports for comparative analysis compared with the benefits of less-structured narrative reports to provide detail and flexibility in reporting;\n**(v)**\nthat summary reports submitted by different covered entities may contain different fields according to the requirements established by the Commission, and the Commission may allow or require submission of incomplete reports;\n**(vi)**\nthat existing data privacy and other regulations may inhibit a covered entity from storing or sharing certain information; and\n**(vii)**\nthat a covered entity may require information from other persons, partnerships, or corporations that develop any covered algorithm by the covered entity for the purpose of performing impact assessment; and\n**(B)**\nmay develop specific requirements for impact assessments and summary reports for particular\u2014\n**(i)**\ncategories of critical decisions, as described in subparagraphs (A) through (I) of section 2(7) or any subcategory developed by the Commission; and\n**(ii)**\nstages of development and deployment of a covered algorithm.\n**(3) Effective date**\nThe regulations described in paragraph (1) shall take effect on the date that is 2 years after such regulations are promulgated.\n#### 4. Requirements for covered entity impact assessment\n##### (a) Requirements for impact assessment\nIn performing any impact assessment required under section 3(b)(1) for a covered algorithm, a covered entity shall do the following, to the extent possible, as applicable to such covered entity as determined by the Commission:\n**(1)**\nIn the case of a new covered algorithm, evaluate any previously existing critical decision-making process used for the same critical decision prior to the deployment of the new covered algorithm, along with any related documentation or information, such as\u2014\n**(A)**\na description of the baseline process being enhanced or replaced by the covered algorithm;\n**(B)**\nany known harm, shortcoming, failure case, or material negative impact on consumers of the previously existing process used to make the critical decision;\n**(C)**\nthe intended benefits of and need for the covered algorithm; and\n**(D)**\nthe intended purpose of the covered algorithm.\n**(2)**\nIdentify and describe any consultation with relevant stakeholders as required by section 3(b)(1)(G), including by documenting\u2014\n**(A)**\nthe points of contact for the stakeholders who were consulted;\n**(B)**\nthe date of any such consultation; and\n**(C)**\ninformation about the terms and process of the consultation, such as\u2014\n**(i)**\nthe existence and nature of any legal or financial agreement between the stakeholders and the covered entity;\n**(ii)**\nany data, system, design, scenario, or other document or material the stakeholder interacted with; and\n**(iii)**\nany recommendations made by the stakeholders that were used to modify the development or deployment of the covered algorithm, as well as any recommendations not used and the rationale for such nonuse.\n**(3)**\nIn accordance with any relevant National Institute of Standards and Technology or other Federal Government best practices and standards, perform ongoing testing and evaluation of the privacy risks and privacy-enhancing measures of the covered algorithm, such as\u2014\n**(A)**\nassessing and documenting the data minimization practices of such algorithm and the duration for which the relevant identifying information and any resulting critical decision is stored;\n**(B)**\nassessing the information security measures in place with respect to such algorithm, including any use of privacy-enhancing technology such as federated learning, differential privacy, secure multi-party computation, de-identification, or secure data enclaves based on the level of risk; and\n**(C)**\nassessing and documenting the current and potential future or downstream positive and negative impacts of such algorithm on the privacy, safety, or security of consumers and their identifying information.\n**(4)**\nPerform ongoing testing and evaluation of the current and historical performance of the covered algorithm using measures such as benchmarking datasets, representative examples from the covered entity\u2019s historical data, and other standards, including by documenting\u2014\n**(A)**\na description of what is deemed successful performance and the methods and technical and business metrics used by the covered entity to assess performance;\n**(B)**\na review of the performance of such algorithm under test conditions or an explanation of why such performance testing was not conducted;\n**(C)**\na review of the performance of such algorithm under deployed conditions or an explanation of why performance was not reviewed under deployed conditions;\n**(D)**\na comparison of the performance of such algorithm under deployed conditions to test conditions or an explanation of why such a comparison was not possible;\n**(E)**\nan evaluation of any differential performance associated with consumers' race, color, sex, gender, age, disability, religion, family status, socioeconomic status, or veteran status, and any other characteristics the Commission deems appropriate (including any combination of such characteristics) for which the covered entity has information, including a description of the methodology for such evaluation and information about and documentation of the methods used to identify such characteristics in the data (such as through the use of proxy data, including ZIP Codes); and\n**(F)**\nif any subpopulations were used for testing and evaluation, a description of which subpopulations were used and how and why such subpopulations were determined to be of relevance for the testing and evaluation.\n**(5)**\nSupport and perform ongoing training and education for all relevant employees, contractors, or other agents regarding any documented material negative impacts on consumers from similar covered algorithms and any improved methods of developing or performing an impact assessment for such algorithm based on industry best practices and relevant proposals and publications from experts, such as advocates, journalists, and academics.\n**(6)**\nAssess the need for and possible development of any guard rail for or limitation on certain uses or applications of the covered algorithm, including whether such uses or applications ought to be prohibited or otherwise limited through any terms of use, licensing agreement, or other legal agreement between entities.\n**(7)**\nMaintain and keep updated documentation of any data or other input information used to develop, test, maintain, or update the covered algorithm, including\u2014\n**(A)**\nhow and when such data or other input information was sourced and, if applicable, licensed, including information such as\u2014\n**(i)**\nmetadata and information about the structure and type of data or other input information, such as the file type, the date of the file creation or modification, and a description of data fields;\n**(ii)**\nan explanation of the methodology by which the covered entity collected, inferred, or obtained the data or other input information and, if applicable, labeled, categorized, sorted, or clustered such data or other input information, including whether such data or other input information was labeled, categorized, sorted, or clustered prior to being collected, inferred, or obtained by the covered entity; and\n**(iii)**\nwhether and how consumers provided informed consent for the inclusion and further use of data or other input information about themselves and any limitations stipulated on such inclusion or further use;\n**(B)**\nwhy such data or other input information was used and what alternatives were explored; and\n**(C)**\nother information about the data or other input information, such as\u2014\n**(i)**\nthe representativeness of the dataset and how this factor was measured, including any assumption about the distribution of the population on which the covered algorithm is deployed; and\n**(ii)**\nthe quality of the data, how the quality was evaluated, and any measure taken to normalize, correct, or clean the data.\n**(8)**\nEvaluate the rights of consumers, such as\u2014\n**(A)**\nby assessing the extent to which the covered entity provides consumers with\u2014\n**(i)**\nclear notice that such algorithm will be used; and\n**(ii)**\na mechanism for opting out of such use;\n**(B)**\nby assessing the transparency and explainability of such algorithm and the degree to which a consumer may contest, correct, or appeal a decision or opt out of such algorithm, including\u2014\n**(i)**\nthe information available to consumers or representatives or agents of consumers about the algorithm, such as any relevant factors that contribute to a particular decision, including an explanation of which contributing factors, if changed, would cause the algorithm to reach a different decision, and how such consumer, representative, or agent can access such information;\n**(ii)**\ndocumentation of any complaint, dispute, correction, appeal, or opt-out request submitted to the covered entity by a consumer with respect to such algorithm; and\n**(iii)**\nthe process and outcome of any remediation measure taken by the covered entity to address the concerns of or harms to consumers; and\n**(C)**\nby describing the extent to which any third-party decision recipient receives a copy of or has access to the results of such algorithm and the category of such third-party decision recipient, as defined by the Commission in section 3(b)(1)(I)(iii).\n**(9)**\nIdentify any likely material negative impact of the covered algorithm on consumers and assess any applicable mitigation strategy, such as by\u2014\n**(A)**\nidentifying and measuring any likely material negative impact of the algorithm on consumers, including documentation of the steps taken to identify and measure such impact;\n**(B)**\ndocumenting any steps taken to eliminate or reasonably mitigate any likely material negative impact identified, including steps such as removing the algorithm from the market or terminating its development;\n**(C)**\nwith respect to the likely material negative impacts identified, documenting which such impacts were left unmitigated and the rationale for the inaction, including details about the justifying non-discriminatory, compelling interest and why such interest cannot be satisfied by other means (such as where there is an equal, zero-sum trade-off between impacts on 2 or more consumers or where the required mitigating action would violate civil rights or other laws); and\n**(D)**\ndocumenting standard protocols or practices used to identify, measure, mitigate, or eliminate any likely material negative impact on consumers and how relevant teams or staff are informed of and trained about such protocols or practices.\n**(10)**\nDescribe any ongoing documentation of the development and deployment process with respect to the covered algorithm, including information such as\u2014\n**(A)**\nthe date of any testing, deployment, licensure, or other significant milestones; and\n**(B)**\npoints of contact for any team, business unit, or similar internal stakeholder that was involved.\n**(11)**\nIdentify any capabilities, tools, standards, datasets, security protocols, improvements to stakeholder engagement, or other resources that may be necessary or beneficial to improving the covered algorithm or the impact assessment of such algorithm, in areas such as\u2014\n**(A)**\nperformance, including accuracy, robustness, and reliability;\n**(B)**\nfairness, including bias and nondiscrimination;\n**(C)**\ntransparency, explainability, contestability, and opportunity for recourse;\n**(D)**\nprivacy and security;\n**(E)**\npersonal and public safety;\n**(F)**\nefficiency and timeliness;\n**(G)**\ncost; or\n**(H)**\nany other area determined appropriate by the Commission.\n**(12)**\nDocument any of the impact assessment requirements described in paragraphs (1) through (11) that were attempted but were not possible to comply with because they were infeasible, as well as the corresponding rationale for not being able to comply with such requirements, which may include\u2014\n**(A)**\nthe absence of certain information about a covered algorithm developed by other persons, partnerships, and corporations;\n**(B)**\nthe absence of certain information about how clients, customers, licensees, partners, and other persons, partnerships, or corporations are deploying a covered algorithm;\n**(C)**\na lack of demographic or other data required to assess differential performance because such data is too sensitive to collect, infer, or store; or\n**(D)**\na lack of certain capabilities, including technological innovations, that would be necessary to conduct such requirements.\n**(13)**\nPerform and document any other ongoing study or evaluation determined appropriate by the Commission.\n##### (b) Rule of construction\nNothing in this Act should be construed to limit any covered entity from adding other criteria, procedures, or technologies to improve the performance of an impact assessment of their covered algorithm.\n##### (c) Nondisclosure of impact assessment\nNothing in this Act should be construed to require a covered entity to share with or otherwise disclose to the Commission or the public any information contained in an impact assessment performed in accordance with this Act, except for any information contained in the summary report required under subparagraph (D) or (E) of section 3(b)(1).\n#### 5. Requirements for summary reports to the Commission\nThe summary report that a covered entity is required to submit under subparagraph (D) or (E) of section 3(b)(1) for any covered algorithm shall, to the extent possible\u2014\n**(1)**\ncontain information from the impact assessment of such algorithm, as applicable, including\u2014\n**(A)**\nthe name, website, and point of contact for the covered entity;\n**(B)**\na detailed description of the specific critical decision that the covered algorithm is intended to make, including the category of critical decision as described in subparagraphs (A) through (I) of section 2(7);\n**(C)**\nthe covered entity's intended purpose for the covered algorithm;\n**(D)**\nan identification of any stakeholders consulted by the covered entity as required by section 3(b)(1)(G) and documentation of the existence and nature of any legal agreements between the stakeholders and the covered entity;\n**(E)**\ndocumentation of the testing and evaluation of the covered algorithm, including\u2014\n**(i)**\nthe methods and technical and business metrics used to assess the performance of such algorithm and a description of what metrics are deemed successful performance;\n**(ii)**\nthe results of any assessment of the performance of such algorithm and a comparison of the results of any assessment under test and deployed conditions; and\n**(iii)**\nan evaluation of any differential performance of such algorithm assessed during the impact assessment;\n**(F)**\nany publicly stated guard rail for or limitation on certain uses or applications of the covered algorithm, including whether such uses or applications ought to be prohibited or otherwise limited through any terms of use, licensing agreement, or other legal agreement between entities;\n**(G)**\ndocumentation about the data or other input information used to develop, test, maintain, or update the covered algorithm including\u2014\n**(i)**\nhow and when the covered entity sourced such data or other input information; and\n**(ii)**\nwhy such data or other input information was used and what alternatives were explored;\n**(H)**\ndocumentation of whether and how the covered entity implements any transparency or explainability measures, including\u2014\n**(i)**\nwhich categories of third-party decision recipients receive a copy of or have access to the results of any decision or judgment that results from such algorithm; and\n**(ii)**\nany mechanism by which a consumer may contest, correct, or appeal a decision or opt out of such algorithm, including the corresponding website for such mechanism, where applicable;\n**(I)**\nany likely material negative impact on consumers identified by the covered entity and a description of the steps taken to remediate or mitigate such impact;\n**(J)**\na list of any impact assessment requirements that were attempted but were not possible to comply with because they were infeasible, as well as the corresponding rationale for not being able to comply with such requirements; and\n**(K)**\nany additional capabilities, tools, standards, datasets, security protocols, improvements to stakeholder engagement, or other resources identified by an impact assessment as necessary or beneficial to improve the performance of impact assessment or the development and deployment of any covered algorithm that the covered entity determines appropriate to share with the Commission;\n**(2)**\ninclude, in addition to the information required under paragraph (1), any relevant additional information from section 4(a) the covered entity wishes to share with the Commission;\n**(3)**\nfollow any format or structure requirements specified by the Commission; and\n**(4)**\ninclude additional criteria that are essential for the purpose of consumer protection, as determined by the Commission.\n#### 6. Reporting; publicly accessible repository\n##### (a) Annual report\nNot later than 1 year after the effective date described in section 3(b)(3), and annually thereafter, the Commission shall publish publicly on the website of the Commission a report describing and summarizing the information from the summary reports submitted under subparagraph (D), (E), or (F) of section 3(b)(1) that\u2014\n**(1)**\nis accessible and machine readable in accordance with the 21st Century Integrated Digital Experience Act ( 44 U.S.C. 3501 note); and\n**(2)**\ndescribes broad trends, aggregated statistics, and anonymized lessons learned about performing impact assessments of covered algorithms, for the purposes of updating guidance related to impact assessments and summary reporting, oversight, and making recommendations to other regulatory agencies.\n##### (b) Publicly accessible repository\n**(1) In general**\n**(A) Establishment**\n**(i) Development**\nNot later than 180 days after the Commission promulgates the regulations required under section 3(b)(1), the Commission shall develop a publicly accessible repository designed to publish a limited subset of the information about each covered algorithm for which the Commission received a summary report under subparagraph (D), (E), or (F) of section 3(b)(1) in order to facilitate consumer protection.\n**(ii) Publication**\nNot later than 180 days after the effective date described in section 3(b)(3), the Commission shall make the repository publicly accessible.\n**(iii) Updates**\nThe Commission shall update the repository on a quarterly basis.\n**(B) Purpose**\nThe purposes of the repository established under subparagraph (A) are\u2014\n**(i)**\nto inform consumers about the use of covered algorithms;\n**(ii)**\nto allow researchers and advocates to study the use of covered algorithms; and\n**(iii)**\nto ensure compliance with the requirements of this Act.\n**(C) Considerations**\nIn establishing the repository under subparagraph (A), the Commission shall consider\u2014\n**(i)**\nhow to provide consumers with pertinent information regarding covered algorithms while minimizing any potential commercial risk to any covered entity of providing such information;\n**(ii)**\nwhat information, if any, to include regarding the specific covered algorithms deployed;\n**(iii)**\nhow to document information, when applicable, about how to contest or seek recourse for a critical decision in a manner that is readily accessible by the consumer; and\n**(iv)**\nhow to streamline the submission of summary reports under subparagraph (D), (E), or (F) of section 3(b)(1) to allow the Commission to efficiently populate information into the repository to minimize or eliminate any burden on the Commission.\n**(D) Requirements**\nThe Commission shall design the repository established under subparagraph (A) to\u2014\n**(i)**\nbe publicly available and easily discoverable on the website of the Commission;\n**(ii)**\nallow users to sort and search the repository by multiple characteristics (such as by covered entity, date reported, or category of critical decision) simultaneously;\n**(iii)**\nallow users to make a copy of or download the information obtained from the repository, including any subsets of information obtained by sorting or searching as described in clause (ii), in accordance with current guidance from the Office of Management and Budget, such as the Open, Public, Electronic, and Necessary Government Data Act ( 44 U.S.C. 101 note);\n**(iv)**\nbe in accordance with user experience and accessibility best practices such as those described in the 21st Century Integrated Digital Experience Act ( 44 U.S.C. 3501 note);\n**(v)**\ninclude a limited subset of information from the summary reports, as applicable, under subparagraph (D), (E), or (F) of section 3(b)(1) that includes\u2014\n**(I)**\nthe identity of the covered entity that submitted such summary report, including any link to the website of the covered entity;\n**(II)**\nthe specific critical decision that the covered algorithm makes, along with the category of the critical decision;\n**(III)**\nany publicly stated prohibited applications of the covered algorithm, including whether such prohibition is enforced through any terms of use, licensing agreement, or other legal agreement between entities;\n**(IV)**\nto the extent possible, the sources of any data used to develop, test, maintain, or update the covered algorithm;\n**(V)**\nto the extent possible, the type of technical and business metrics used to assess the performance of the covered algorithm when deployed; and\n**(VI)**\nthe link to any web page with instructions or other information related to a mechanism by which a consumer may contest, correct, or appeal a decision or opt out of the covered algorithm; and\n**(vi)**\ninclude information about design, use, and maintenance of the repository, including\u2014\n**(I)**\nhow frequently the repository is updated;\n**(II)**\nthe date of the most recent such update;\n**(III)**\nthe types of information from the summary reports submitted under subparagraph (D), (E), or (F) of section 3(b)(1) that are and are not included in the repository; and\n**(IV)**\nany other information about the design, use, and maintenance the Commission determines is\u2014\n**(aa)**\nrelevant to consumers and researchers; or\n**(bb)**\nessential for consumer education and recourse.\n**(2) Authorization of appropriations**\nThere are authorized to be appropriated to the Commission such sums as are necessary to carry out this subsection.\n#### 7. Guidance and technical assistance; other requirements\n##### (a) Guidance and technical assistance from the Commission\n**(1) In general**\nThe Commission shall publish guidance on how to meet the requirements of sections 4 and 5, including resources such as documentation templates and guides for meaningful consultation, that is developed by the Commission after consultation with the Director of the National Institute of Standards and Technology, the Director of the National Artificial Intelligence Initiative, the Director of the Office of Science and Technology Policy, and other relevant stakeholders, including standards bodies, private industry, academia, technology experts, and advocates for civil rights, consumers, and impacted communities.\n**(2) Assistance in determining covered entity status**\nIn addition to the guidance required under paragraph (1), the Commission shall\u2014\n**(A)**\nissue guidance and training materials to assist persons, partnerships, and corporations in evaluating whether they are a covered entity; and\n**(B)**\nregularly update such guidance and training materials in accordance with any feedback or questions from covered entities, experts, or other relevant stakeholders.\n##### (b) Other requirements\n**(1) Publication**\nNothing in this Act shall be construed to limit a covered entity from publicizing any documentation of the impact assessment maintained under section 3(b)(1)(B), including information beyond what is required to be submitted in a summary report under subparagraph (D) or (E) of section 3(b)(1), unless such publication would violate the privacy of any consumer.\n**(2) Periodic review of regulations**\nThe Commission shall review the regulations promulgated under section 3(b) not less than once every 5 years and update such regulations as appropriate.\n**(3) Review by NIST and OSTP**\nThe Commission shall make available, in a private and secure manner, to the Director of the National Institute of Standards and Technology, the Director of the Office of Science and Technology Policy, and the head of any Federal agency with relevant regulatory jurisdiction over a covered algorithm any summary report submitted under subparagraph (D), (E), or (F) of section 3(b)(1) for review in order to develop future standards or regulations.\n#### 8. Resources and authorities\n##### (a) Bureau of Technology\n**(1) Establishment**\n**(A) In general**\nThere is established within the Commission the Bureau of Technology (in this subsection referred to as the Bureau ).\n**(B) Duties**\nThe Bureau shall engage in activities that include:\n**(i)**\nAiding or advising the Commission with respect to the technological aspects of the functions of the Commission, including\u2014\n**(I)**\npreparing, conducting, facilitating, managing, or otherwise enabling studies, workshops, audits, community participation opportunities, or other similar activities; and\n**(II)**\nany other assistance deemed appropriate by the Commission or Chair.\n**(ii)**\nAiding or advising the Commission with respect to the enforcement of this Act.\n**(iii)**\nProviding technical assistance to any enforcement bureau within the Commission with respect to the investigation and trial of cases.\n**(2) Chief Technologist**\nThe Bureau shall be headed by a Chief Technologist.\n**(3) Staff**\n**(A) Appointments**\n**(i) In general**\nSubject to subparagraph (B), the Chair may, without regard to the civil service laws (including regulations), appoint personnel with experience in fields such as management, technology, digital and product design, user experience, information security, civil rights, technology policy, privacy policy, humanities and social sciences, product management, software engineering, machine learning, statistics, or other related fields to enable the Bureau to perform its duties.\n**(ii) Minimum appointments**\nNot later than 2 years after the date of enactment of this Act, the Chair shall appoint not less than 50 personnel.\n**(B) Excepted service**\nThe personnel appointed in accordance with subparagraph (A) may be appointed to positions described in section 213.3102(r) of title 5, Code of Federal Regulations.\n**(4) Authorization of appropriations**\nThere are authorized to be appropriated to the Commission such sums as are necessary to carry out this subsection.\n##### (b) Additional personnel in the Bureau of Consumer Protection\n**(1) Additional personnel**\nNotwithstanding any other provision of law, the Chair may, without regard to the civil service laws (including regulations), appoint 25 additional personnel to the Division of Enforcement of the Bureau of Consumer Protection.\n**(2) Authorization of appropriations**\nThere are authorized to be appropriated to the Commission such sums as are necessary to carry out this subsection.\n##### (c) Establishment of agreements of cooperation\nThe Commission shall negotiate agreements of cooperation, as needed, with any relevant Federal agency with respect to information sharing and enforcement actions taken regarding the development or deployment of a covered algorithm to make a critical decision. Such agreements shall include procedures for determining which agency shall file an action and providing notice to the non-filing agency, where feasible, prior to initiating a civil action to enforce any Federal law within such agencies' jurisdictions regarding the development or deployment of a covered algorithm to make a critical decision by a covered entity.\n#### 9. Enforcement\n##### (a) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act or a regulation promulgated thereunder shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act and the regulations promulgated under this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates this Act or a regulation promulgated thereunder shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n**(D) Rulemaking**\nThe Commission shall promulgate in accordance with section 553 of title 5, United States Code, such additional rules as may be necessary to carry out this Act.\n##### (b) Enforcement by States\n**(1) In general**\nIf the attorney general of a State has reason to believe that an interest of the residents of the State has been or is being threatened or adversely affected by a practice that violates this Act or a regulation promulgated thereunder, the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief.\n**(2) Rights of Commission**\n**(A) Notice to Commission**\n**(i) In general**\nExcept as provided in clause (iii), the attorney general of a State, before initiating a civil action under paragraph (1), shall provide written notification to the Commission that the attorney general intends to bring such civil action.\n**(ii) Contents**\nThe notification required under clause (i) shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required under clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention by Commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by the attorney general of a State under paragraph (1); and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal of a decision in the civil action.\n**(3) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(4) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which\u2014\n**(i)**\nthe defendant is an inhabitant, may be found, or transacts business; or\n**(ii)**\nvenue is proper under section 1391 of title 28, United States Code.\n**(5) Actions by other State officials**\n**(A) In general**\nIn addition to a civil action brought by an attorney general under paragraph (1), any other officer of a State who is authorized by the State to do so may bring a civil action under paragraph (1), subject to the same requirements and limitations that apply under this subsection to civil actions brought by attorneys general.\n**(B) Savings provision**\nNothing in this subsection may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n#### 10. Coordination\nIn carrying out this Act, the Commission shall coordinate with any appropriate Federal agency or State regulator to promote consistent regulatory treatment of covered algorithms.\n#### 11. No preemption\nNothing in this Act may be construed to preempt any State, tribal, city, or local law, regulation, or ordinance.",
      "versionDate": "2025-09-19",
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
        "actionDate": "2025-06-25",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2164",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Algorithmic Accountability Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-09T22:14:44Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5511ih.xml"
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
      "title": "Algorithmic Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Algorithmic Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Federal Trade Commission to require impact assessments of certain algorithms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:15Z"
    }
  ]
}
```
