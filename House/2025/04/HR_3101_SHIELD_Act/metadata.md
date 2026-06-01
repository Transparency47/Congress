# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3101?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3101
- Title: SHIELD Act
- Congress: 119
- Bill type: HR
- Bill number: 3101
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-03-27T08:06:35Z
- Update date including text: 2026-03-27T08:06:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3101",
    "number": "3101",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000598",
        "district": "42",
        "firstName": "Robert",
        "fullName": "Rep. Garcia, Robert [D-CA-42]",
        "lastName": "Garcia",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SHIELD Act",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:35Z",
    "updateDateIncludingText": "2026-03-27T08:06:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MN"
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
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "OR"
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
      "sponsorshipDate": "2025-05-13",
      "state": "DC"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MI"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3101ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3101\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Garcia of California (for himself, Mrs. Torres of California , Mrs. Ramirez , Ms. Vel\u00e1zquez , Mr. Frost , Mr. Espaillat , Ms. Lee of Pennsylvania , Ms. Omar , Ms. Barrag\u00e1n , Mr. Goldman of New York , and Ms. Salinas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the Attorney General to provide grants to States, units of local government, and organizations to support the recruitment, training, and development of staff and infrastructure needed to support the due process rights of individuals facing deportation.\n#### 1. Short title\nThis Act may be cited as the Securing Help for Immigrants through Education and Legal Development Act or the SHIELD Act .\n#### 2. Definitions\nIn this Act:\n**(1) Service area**\nThe term service area means the jurisdiction or geographical area in which an entity carries out activities using funds awarded under this Act.\n**(2) State**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n**(3) Unit of local government**\nThe term unit of local government has the meaning given such term in section 901(a)(3) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251(a)(3) ).\n**(4) Individual facing deportation**\nThe term individual facing deportation means an individual in a proceeding under section 212(d)(5)(A), 235(b)(1)(B), 236, 238, 240, or 241 of the Immigration and Nationality Act.\n#### 3. Sense of Congress on access to legal counsel\nIt is the sense of Congress that\u2014\n**(1)**\nunlike in the criminal legal system, there is no right to government-funded legal representation for people facing the devastating consequences of detention and deportation who cannot afford a lawyer, even children are not entitled to an attorney in these complex proceedings;\n**(2)**\nas a result, most people in removal proceedings, including an estimated 80 percent of individuals held in immigration detention during deportation cases initiated in the past 20 years, are unrepresented and are forced to navigate the complexities of immigration law against trained government prosecutors alone;\n**(3)**\nthe consequences of detention or deportation are devastating, and can include the loss of liberty, the denial of lawful immigration status or United States citizenship, loss of livelihood, separation from and inability to support family, and life-threatening danger in the country of origin;\n**(4)**\nlegal representation has been proven to significantly increase the likelihood of someone being released from detention on bond and establishing a right to remain in the United States;\n**(5)**\nstudies show that detained immigrants with attorneys are 3.5 times more likely to be granted bond and people in detention with representation are up to 10.5 times more likely to obtain relief from deportation than those without representation, controlling for other factors;\n**(6)**\nfor nondetained people, 60 percent of individuals with lawyers win their cases compared to 17 percent of those without a lawyer;\n**(7)**\nthe detention and deportation system disproportionately impacts Black immigrants and reinforces systemic racism, and ensuring that immigrants have access to a lawyer reduces the harms of the racial inequities in the immigration system;\n**(8)**\nsince 2013, local and State governments have led the charge on providing public funding for deportation defense for their residents facing deportation, with over 55 local and State governments, including 10 States, funding these programs;\n**(9)**\nthe success of local and State publicly funded deportation defense programs demonstrate the positive impact that publicly funded universal representation programs have on improving individual outcomes, keeping families and communities together, and avoiding the resulting social, economic, and public health costs of deportation;\n**(10)**\nwhile these local and State programs have made a significant impact, they are insufficient to meet the need for representation and the Federal Government must act to address the significant unmet need for legal defense in the Federal immigration system by passing the Fairness to Freedom Act of 2023, which establishes a universal right to federally funded representation for anyone facing deportation, regardless of the individual\u2019s ability to pay;\n**(11)**\nthe growth of these local and State programs and the resulting staffing recruitment challenges have also further highlighted the acute need to develop and grow a legal and social services staffing and infrastructure to address the unmet representational needs for immigrants facing deportation;\n**(12)**\ninfrastructure must be built to maintain a highly skilled and sustainable legal defense workforce equipped with the tools to implement high-quality, independent legal representation regardless of the individual\u2019s ability to pay, prior contact with the criminal legal system, or the nature or perceived strength of their legal defense; and\n**(13)**\nin its 2023 Report Access to Justice in Federal Administrative Proceedings , the Legal Aid Interagency Roundtable outlines the harms that unrepresented individuals face in Federal administrative proceedings, including immigration court, and their core strategy of increasing representation and assistance by lawyers and nonlawyers for people in administrative proceedings.\n#### 4. Immigration legal services staff and infrastructure development program\n##### (a) In general\nThe Attorney General, acting through the Director of the Office of Access to Justice, shall award competitive workforce development and capacity building grants to eligible entities that are seeking to expand access to representation for individuals facing deportation by increasing the workforce and strengthening the legal services infrastructure needed to provide such representation.\n##### (b) Eligibility criteria\nAn entity eligible to receive a grant under this section is a\u2014\n**(1)**\nState or unit of local government that has allocated public funds towards the provision of immigration-related legal services, including legal representation, legal assistance, community navigation, and related services, to individuals facing deportation;\n**(2)**\na community-based organization, nonprofit organization, or educational institution that provides or coordinates immigration-related legal services to individuals facing deportation; or\n**(3)**\na community-based organization, nonprofit organization, or educational institution that recruits, trains, or mentors individuals who provide or will provide immigration-related legal services to individuals facing deportation.\n##### (c) Application\nAn eligible entity seeking a grant under this section shall submit to the Director of the Office of Access to Justice an application at such time, in such manner, and containing such information as the Director may reasonably require.\n##### (d) Use of funds\nFunds awarded under this section shall be used to develop a workforce scaled to meet the representation needs of all individuals facing deportation, grow the immigration-related legal services infrastructure, and enhance long-term capacity to provide high-quality, holistic, and linguistically appropriate legal services, which may include\u2014\n**(1)**\nworkforce recruitment and training programs, such as educational, fellowship, clinical, job recruitment, and job training services aimed at increasing the number of lawyers, accredited representatives, social workers, and community navigators entering the immigration legal services field;\n**(2)**\ntechnical assistance services, such as\u2014\n**(A)**\nsubstantive and technical skills-based trainings to improve the quality of representation provided to individuals facing deportation;\n**(B)**\nlanguage training to ensure legal staff are equipped to provide linguistically appropriate services;\n**(C)**\nspecialized legal support to support representation in complex defense cases, including representation in Federal court and State court; and\n**(D)**\nleadership development, including management training and establishing appropriate supervisory systems;\n**(3)**\nlocal or regional coordination services to ensure a coordinated and efficient delivery of legal services to individuals facing deportation;\n**(4)**\nretention improvement strategies to ensure sustainable growth of the immigration-related legal services field, including strategies to address caseload management, burnout, and organizational systems;\n**(5)**\nrecruiting and retaining legal staff from underrepresented backgrounds and promoting diversity within the legal services field;\n**(6)**\ngrowing legal services infrastructure and representational capacity in locations with a significant unmet need for legal representation and with significantly less immigration-related legal services capacity in their service area than national averages; and\n**(7)**\nphysical, administrative, and technological infrastructure resources in coordination with a use of funds described in paragraphs (1) through (6).\n##### (e) Contracts and subawards\nA recipient of a grant under this section may, for purposes authorized under subsection (d), use all or a portion of that grant to contract with or make one or more subawards to one or more\u2014\n**(1)**\ncommunity-based organization, nonprofit organization, private organization, or educational institution; or\n**(2)**\nunits of local government.\n##### (f) Conditions\nAs a condition of receiving a grant under this section, an eligible entity shall\u2014\n**(1)**\nsubmit to the Attorney General a certification that the proposed uses of grant funds by the entity\u2014\n**(A)**\nare consistent with this section; and\n**(B)**\nmeet the criteria determined by the Attorney General, in consultation with the Director of the Office of Access to Justice; and\n**(2)**\nnot later than 90 days after the end of each fiscal year for which an entity receives grant funds under this section, submit to the Director of the Office of Access to Justice a report that describes\u2014\n**(A)**\nthe types of services being provided under the grant;\n**(B)**\nthe service area;\n**(C)**\nthe number of individuals recruited or retained through services funded under the grant;\n**(D)**\nthe impact that staffing recruitment and retention has had on organizational capacity to represent more individuals within the service area;\n**(E)**\nthe actual expenditures made in connection with the grant, including personnel and staffing structure and indirect costs;\n**(F)**\nthe outcomes of services; and\n**(G)**\na description of the continuing unmet representation needs of individuals facing deportation in the service area and recommendations of supports and resources needed to meet them.\n##### (g) Grant term\nThe term of a grant under this section shall be 4 years, and such grant may be renewed.\n##### (h) Supplement of Non-Federal Funds\nAny Federal funds received under this section shall be used to supplement, not supplant, Federal or non-Federal funds that would otherwise be available for activities funded under this section.\n#### 5. Authority and duties of the administering agency\n##### (a) Duties of the Director\nThe Director of the Office of Access to Justice may promulgate such rules, policies, and procedures as may be necessary and appropriate to carry out the grant program under this Act, including the following:\n**(1)**\nEstablishing competitive grantmaking procedures to identify grant recipients.\n**(2)**\nTargeting grants in a manner that best accomplishes the following objectives and priorities:\n**(A)**\nAdvancing a legal services workforce trained and equipped to implement an independent legal defense for individuals facing deportation that ensures high-quality, independent legal representation, regardless of ability to pay, prior contact with the criminal legal system, or the nature or perceived strength of their legal defense.\n**(B)**\nA national legal services infrastructure scaled to meet the representation needs of all individuals facing deportation.\n**(C)**\nLong-term growth of organizational or programmatic capacity to provide high-quality, holistic, and linguistically appropriate legal services to individuals facing deportation.\n**(D)**\nProviding support to State and local governments that have taken leadership and developed expertise in providing public funding for the legal defense of individuals facing deportation.\n**(E)**\nAddressing the crisis of lack of representation in parts of the country where such publicly funded programs have not been established.\n##### (b) Independent implementation\nExcept as otherwise provided in this Act, the Attorney General, acting through the Director, shall exercise the authority under this Act in an independent manner in order to advance the primary objective of increasing access to representation for individuals facing deportation, and without regard to other priorities of the Federal Government related to immigration enforcement.\n#### 6. Reports and accountability\n##### (a) Reports and evaluations\nFor each fiscal year, each grantee under this section during that fiscal year shall submit to the Attorney General a report on the effectiveness of activities carried out using such grant. Each report shall include an evaluation in such form and containing such information as the Attorney General may reasonably require. The Attorney General shall specify the dates on which such reports shall be submitted.\n##### (b) Accountability\nGrants awarded under this Act shall be subject to the following accountability provisions:\n**(1) Audit requirement**\n**(A) Definition**\nIn this paragraph, the term unresolved audit finding means a finding in the final audit report of the Inspector General of the Department of Justice under subparagraph (C) that the audited grantee has used grant funds for an unauthorized expenditure or otherwise unallowable cost that is not closed or resolved within 1 year after the date on which 1 final audit report is issued.\n**(B) Audits**\nBeginning in the first fiscal year beginning after December 13, 2016, and in each fiscal year thereafter, the Inspector General of the Department of Justice shall conduct audits of grantees under this section to prevent waste, fraud, and abuse of funds by grantees. The Inspector General shall determine the appropriate number of grantees to be audited each year.\n**(C) Final audit report**\nThe Inspector General of the Department of Justice shall submit to the Attorney General a final report on each audit conducted under subparagraph (B).\n**(D) Technical assistance**\nA recipient of a grant under this section that is found to have an unresolved audit finding shall be eligible to receive prompt, individualized technical assistance to resolve the audit finding and to prevent future findings, for a period not to exceed the following 2 fiscal years.\n**(E) Priority**\nIn making grants under this section, the Attorney General shall give priority to applicants that did not have an unresolved audit finding during the 3 fiscal years before submitting an application for a grant under this section.\n**(2) Nonprofit agency requirements**\n**(A) Definition**\nFor purposes of this paragraph and the grant program under this section, the term nonprofit agency means an organization that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of the Internal Revenue Code of 1986.\n**(B) Prohibition**\nThe Attorney General may not award a grant under this section to a nonprofit agency that holds money in an offshore account for the purpose of avoiding paying the tax described in section 511(a) of the Internal Revenue Code of 1986.\n**(C) Disclosure**\nEach nonprofit agency that is awarded a grant under this section and uses the procedures prescribed in regulations to create a rebuttable presumption of reasonableness for the compensation of its officers, directors, trustees, and key employees, shall disclose to the Attorney General, in the application for the grant, the process for determining such compensation, including the independent persons involved in reviewing and approving such compensation, the comparability data used, and contemporaneous substantiation of the deliberation and decision. Upon request, the Attorney General shall make the information disclosed under this subparagraph available for public inspection.\n**(3) Conference expenditures**\n**(A) Limitation**\nNot more than $100,000 of the amounts made available to the Department of Justice to carry out this section may be used by the Attorney General, or by any individual or entity awarded a grant under this section to host, or make any expenditures relating to, a conference unless the Deputy Attorney General provides prior written authorization that the funds may be expended to host the conference or make such expenditure.\n**(B) Written approval**\nWritten approval under subparagraph (A) shall include a written estimate of all costs associated with the conference, including the cost of all food, beverages, audio-visual equipment, honoraria for speakers, and entertainment.\n**(C) Report**\nThe Deputy Attorney General shall submit an annual report to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives on all conference expenditures approved under this paragraph.\n**(4) Annual certification**\nBeginning in the first fiscal year beginning after the date of enactment of this Act, the Attorney General shall submit to the Committee on the Judiciary and the Committee on Appropriations of the Senate and the Committee on the Judiciary and the Committee on Appropriations of the House of Representatives an annual certification indicating whether all final audit reports issued by the Office of the Inspector General under paragraph (1) have been completed and reviewed by the appropriate Assistant Attorney General or Director.\n#### 7. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $100,000,000 for each of fiscal years 2026 through 2027.",
      "versionDate": "2025-04-30",
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
        "name": "Immigration",
        "updateDate": "2025-05-22T13:07:09Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3101ih.xml"
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
      "title": "SHIELD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:08Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHIELD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Help for Immigrants through Education and Legal Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Attorney General to provide grants to States, units of local government, and organizations to support the recruitment, training, and development of staff and infrastructure needed to support the due process rights of individuals facing deportation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:37Z"
    }
  ]
}
```
