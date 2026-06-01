# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4142?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4142
- Title: SHIELD Act
- Congress: 119
- Bill type: S
- Bill number: 4142
- Origin chamber: Senate
- Introduced date: 2026-03-19
- Update date: 2026-04-01T17:00:53Z
- Update date including text: 2026-04-01T17:00:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in Senate
- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-19: Introduced in Senate

## Actions

- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4142",
    "number": "4142",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "SHIELD Act",
    "type": "S",
    "updateDate": "2026-04-01T17:00:53Z",
    "updateDateIncludingText": "2026-04-01T17:00:53Z"
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
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-19",
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
        "item": {
          "date": "2026-03-19T16:52:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4142is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4142\nIN THE SENATE OF THE UNITED STATES\nMarch 19, 2026 Mr. Markey (for himself, Mr. Padilla , Mr. Schiff , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize the Attorney General to provide grants to States, units of local government, and organizations to support the recruitment, training, and development of staff and infrastructure needed to support the due process rights of individuals facing removal.\n#### 1. Short titles\nThis Act may be cited as the Securing Help for Immigrants through Education and Legal Development Act or the SHIELD Act .\n#### 2. Definitions\nIn this Act:\n**(1) Individual facing removal**\nThe term individual facing removal means an individual in a proceeding under section 235(b), 238, 240, or 241(a)(5) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b) , 1228, 1229a, and 1231(a)(5)).\n**(2) Service area**\nThe term service area means the jurisdiction or geographical area in which an entity carries out activities using funds awarded under this Act.\n**(3) State**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n**(4) Unit of local government**\nThe term unit of local government has the meaning given such term in section 901(a)(3) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251(a)(3) ).\n#### 3. Immigration legal services staff and infrastructure development program\n##### (a) In general\nThe Attorney General, acting through the Director of the Office for Access to Justice, shall award competitive workforce development and capacity building grants to eligible entities that are seeking to expand access to representation for individuals facing removal by increasing the workforce and strengthening the legal services infrastructure needed to provide such representation.\n##### (b) Eligibility criteria\nAn entity is eligible to receive a grant under this section if it is a\u2014\n**(1)**\nState or unit of local government that has allocated public funds towards the provision of immigration-related legal services, including legal representation, legal assistance, community navigation, and related services, to individuals facing removal;\n**(2)**\na community-based organization, nonprofit organization, or educational institution that provides or coordinates immigration-related legal services to individuals facing removal; or\n**(3)**\na community-based organization, nonprofit organization, or educational institution that recruits, trains, or mentors individuals who provide or will provide immigration-related legal services to individuals facing removal.\n##### (c) Application\nAn eligible entity seeking a grant under this section shall submit to the Director of the Office for Access to Justice an application at such time, in such manner, and containing such information as the Director may reasonably require.\n##### (d) Use of funds\nFunds awarded under this section shall be used to develop a workforce scaled to meet the representation needs of all individuals facing removal, grow the immigration-related legal services infrastructure, and enhance long-term capacity to provide high-quality, holistic, and linguistically appropriate legal services, which may include\u2014\n**(1)**\nworkforce recruitment and training programs, such as educational, fellowship, clinical, job recruitment, and job training services aimed at increasing the number of lawyers, accredited representatives, social workers, and community navigators entering the immigration legal services field;\n**(2)**\ntechnical assistance services, such as\u2014\n**(A)**\nsubstantive and technical skills-based trainings to improve the quality of representation provided to individuals facing removal;\n**(B)**\nlanguage training to ensure legal staff are equipped to provide linguistically appropriate services;\n**(C)**\nspecialized legal support to support representation in complex defense cases, including representation in Federal court and State court; and\n**(D)**\nleadership development, including management training and establishing appropriate supervisory systems;\n**(3)**\nlocal or regional coordination services to ensure a coordinated and efficient delivery of legal services to individuals facing removal;\n**(4)**\nretention improvement strategies to ensure sustainable growth of the immigration-related legal services field, including strategies to address caseload management, burnout, and organizational systems;\n**(5)**\nrecruiting and retaining legal staff from underrepresented backgrounds and promoting diversity within the legal services field;\n**(6)**\ngrowing legal services infrastructure and representational capacity in locations with a significant unmet need for legal representation and with significantly less immigration-related legal services capacity in their service area than national averages; and\n**(7)**\nphysical, administrative, and technological infrastructure resources in coordination with a use of funds described in paragraphs (1) through (6).\n##### (e) Contracts and subawards\nA recipient of a grant under this section may, for purposes authorized under subsection (d), use all or a portion of that grant to contract with or make one or more subawards to one or more\u2014\n**(1)**\ncommunity-based organization, nonprofit organization, private organization, or educational institution; or\n**(2)**\nunits of local government.\n##### (f) Conditions\nAs a condition of receiving a grant under this section, an eligible entity shall\u2014\n**(1)**\nsubmit to the Attorney General a certification that the proposed uses of grant funds by the entity\u2014\n**(A)**\nare consistent with this section; and\n**(B)**\nmeet the criteria determined by the Attorney General, in consultation with the Director of the Office for Access to Justice; and\n**(2)**\nnot later than 90 days after the end of each fiscal year for which an entity receives grant funds under this section, submit a report to the Director of the Office for Access to Justice that describes\u2014\n**(A)**\nthe types of services being provided under the grant;\n**(B)**\nthe service area;\n**(C)**\nthe number of individuals recruited or retained through services funded under the grant;\n**(D)**\nthe impact that staffing recruitment and retention has had on organizational capacity to represent more individuals within the service area;\n**(E)**\nthe actual expenditures made in connection with the grant, including personnel and staffing structure and indirect costs;\n**(F)**\nthe outcomes of services; and\n**(G)**\na description of the continuing unmet representation needs of individuals facing removal in the service area and recommendations of supports and resources needed to meet them.\n##### (g) Grant term\nThe term of a grant under this section shall be 4 years, which may be renewed.\n##### (h) Supplement of Non-Federal Funds\nAny Federal funds received under this section shall be used to supplement, not supplant, Federal or non-Federal funds that would otherwise be available for activities funded under this section.\n#### 4. Authority and duties of the administering agency\n##### (a) Duties of the Director\nThe Director of the Office for Access to Justice may promulgate such rules, policies, and procedures as may be necessary and appropriate to carry out the grant program under this Act, including the following:\n**(1)**\nEstablishing competitive grantmaking procedures to identify grant recipients.\n**(2)**\nTargeting grants in a manner that best accomplishes the following objectives and priorities:\n**(A)**\nAdvancing a legal services workforce trained and equipped to implement an independent legal defense for individuals facing removal that ensures high-quality, independent legal representation, regardless of ability to pay, prior contact with the criminal legal system, or the nature or perceived strength of their legal defense.\n**(B)**\nA national legal services infrastructure scaled to meet the representation needs of all individuals facing removal.\n**(C)**\nLong-term growth of organizational or programmatic capacity to provide high-quality, holistic, and linguistically appropriate legal services to individuals facing removal.\n**(D)**\nProviding support to State and local governments that have taken leadership and developed expertise in providing public funding for the legal defense of individuals facing removal.\n**(E)**\nAddressing the crisis of lack of representation in parts of the country where such publicly funded programs have not been established.\n##### (b) Independent implementation\nExcept as otherwise provided in this Act, the Attorney General, acting through the Director of the Office for Access to Justice, shall exercise the authority under this Act in an independent manner in order to advance the primary objective of increasing access to representation for individuals facing removal, and without regard to other priorities of the Federal Government related to immigration enforcement.\n#### 5. Reports and accountability\n##### (a) Reports and evaluations\nFor each fiscal year, each grantee under this section during that fiscal year shall submit to the Attorney General a report on the effectiveness of activities carried out using such grant. Each report shall include an evaluation in such form and containing such information as the Attorney General may reasonably require. The Attorney General shall specify the dates on which such reports shall be submitted.\n##### (b) Accountability\nGrants awarded under this Act shall be subject to the following accountability provisions:\n**(1) Audit requirement**\n**(A) Defined term**\nIn this paragraph, the term unresolved audit finding means a finding in the final audit report of the Inspector General of the Department of Justice under subparagraph (C) that the audited grantee has used grant funds for an unauthorized expenditure or otherwise unallowable cost that is not closed or resolved within 1 year after the date on which 1 final audit report is issued.\n**(B) Audits**\nBeginning in the first fiscal year beginning after December 13, 2016, and in each fiscal year thereafter, the Inspector General of the Department of Justice shall conduct audits of grantees under this section to prevent waste, fraud, and abuse of funds by grantees. The Inspector General shall determine the appropriate number of grantees to be audited each year.\n**(C) Final audit report**\nThe Inspector General of the Department of Justice shall submit to the Attorney General a final report on each audit conducted under subparagraph (B).\n**(D) Technical assistance**\nA recipient of a grant under this section that is found to have an unresolved audit finding shall be eligible to receive prompt, individualized technical assistance to resolve the audit finding and to prevent future findings, for a period not to exceed the following 2 fiscal years.\n**(E) Priority**\nIn making grants under this section, the Attorney General shall give priority to applicants that did not have an unresolved audit finding during the 3 fiscal years before submitting an application for a grant under this section.\n**(2) Nonprofit agency requirements**\n**(A) Defined term**\nFor purposes of this paragraph and the grant program authorized under this section, the term nonprofit agency means an organization that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of the Internal Revenue Code of 1986.\n**(B) Prohibition**\nThe Attorney General may not award a grant under this section to a nonprofit agency that holds money in an offshore account for the purpose of avoiding paying the tax described in section 511(a) of the Internal Revenue Code of 1986.\n**(C) Disclosure**\nEach nonprofit agency that is awarded a grant under this section and uses the procedures prescribed in regulations to create a rebuttable presumption of reasonableness for the compensation of its officers, directors, trustees, and key employees, shall disclose to the Attorney General, in the application for the grant, the process for determining such compensation, including the independent persons involved in reviewing and approving such compensation, the comparability data used, and contemporaneous substantiation of the deliberation and decision. Upon request, the Attorney General shall make the information disclosed under this subparagraph available for public inspection.\n**(3) Conference expenditures**\n**(A) Limitation**\nNot more than $100,000 of the amounts made available to the Department of Justice to carry out this section may be used by the Attorney General, or by any individual or entity awarded a grant under this section to host, or make any expenditures relating to, a conference unless the Deputy Attorney General provides prior written authorization that the funds may be expended to host the conference or make such expenditure.\n**(B) Written approval**\nWritten approval under subparagraph (A) shall include a written estimate of all costs associated with the conference, including the cost of all food, beverages, audio-visual equipment, honoraria for speakers, and entertainment.\n**(C) Report**\nThe Deputy Attorney General shall submit an annual report to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives on all conference expenditures approved under this paragraph.\n**(4) Annual certification**\nBeginning in the first fiscal year beginning after the date of the enactment of this Act, the Attorney General shall submit an annual certification to the Committee on the Judiciary of the Senate , the Committee on Appropriations of the Senate , the Committee on the Judiciary of the House of Representatives , and the Committee on Appropriations of the House of Representatives that indicates whether all final audit reports issued by the Office of the Inspector General under paragraph (1) have been completed and reviewed by the appropriate Assistant Attorney General or the Director of the Office for Access to Justice.\n#### 6. Authorization of appropriations\nThere is authorized to be appropriated to the Department of Justice to carry out this Act $100,000,000 for each of the fiscal years 2026 through 2027.\n#### 7. Rules of construction\nNothing in this Act may be construed to preclude the ability for a respondent to obtain counsel at no expense to the Government pursuant to sections 240(b)(4) and 292 of the Immigration and Nationality Act ( 8 U.S.C. 1229a(b)(4) and 8 U.S.C. 1362 ).",
      "versionDate": "2026-03-19",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-04-01T17:00:53Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4142is.xml"
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
      "title": "SHIELD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SHIELD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing Help for Immigrants through Education and Legal Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Attorney General to provide grants to States, units of local government, and organizations to support the recruitment, training, and development of staff and infrastructure needed to support the due process rights of individuals facing removal.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T05:18:33Z"
    }
  ]
}
```
