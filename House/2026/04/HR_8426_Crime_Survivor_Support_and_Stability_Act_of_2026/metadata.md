# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8426?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8426
- Title: Crime Survivor Support and Stability Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8426
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-05-01T18:34:49Z
- Update date including text: 2026-05-01T18:34:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8426",
    "number": "8426",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001231",
        "district": "12",
        "firstName": "Lateefah",
        "fullName": "Rep. Simon, Lateefah [D-CA-12]",
        "lastName": "Simon",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Crime Survivor Support and Stability Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-01T18:34:49Z",
    "updateDateIncludingText": "2026-05-01T18:34:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:02:20Z",
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
          "date": "2026-04-21T14:02:15Z",
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
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "OH"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "GA"
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
      "sponsorshipDate": "2026-04-21",
      "state": "DC"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8426ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8426\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Ms. Simon (for herself, Mrs. Sykes , Mr. Johnson of Georgia , Ms. Norton , Mrs. Dingell , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo encourage States to provide rights to survivors of violence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Crime Survivor Support and Stability Act of 2026 .\n#### 2. Rights of survivors of violence\nIt is the sense of the Congress that each State should review and revise, if necessary, its laws to ensure that survivors of violence receive the healing, safety, and support they require after a victimization, taking into account the following:\n**(1)**\nA survivor of violence should be accorded the following rights:\n**(A)**\nA right to trusted and accessible community-based help to heal from trauma, including for adult and minor survivors.\n**(B)**\nA right to programs that offer emergency and flexible financial help quickly, without burdensome administrative or exclusionary restrictions.\n**(C)**\nA right to stable housing, including the right to break a lease without penalty, or be protected from eviction.\n**(D)**\nA right to paid and job-protected leave time off from work to address safety, medical, financial, emotional, and other recovery, healing, and safety needs related to the victimization.\n**(E)**\nA right to debt forgiveness and financial recovery in the case of a debt that is related to the victimization.\n**(F)**\nA right to legal assistance related to housing, job, immigration, or family legal issues.\n**(G)**\nA right to request and access community-based alternative accountability or resolution processes, instead of prosecution in the criminal justice system.\n**(H)**\nA right to protection from arrest or conviction for survivors criminalized as a result of victimization, and to mitigated sentencing and record clearance for convicted survivors whose offense was related to trauma.\n**(2)**\nThe rights of a survivor of violence under paragraph (1) should not be contingent on or in any way limited or restricted by the following:\n**(A)**\nA condition that the survivor or anyone else has reported the victimization to a law enforcement agency, court, or other local, State, or Federal agency designated to investigate or prosecute crimes, abuse, or violence.\n**(B)**\nA condition that the survivor or a family member of the survivor cooperate with a law enforcement agency, court, or other local, State, or Federal agency designated to investigate or prosecute crimes, abuse, or violence.\n**(C)**\nA survivor\u2019s race, religion, national origin, sex, age, disability, sexual orientation, gender identity, marital status, immigration status, housing status, economic status, or family status.\n**(D)**\nWhether a survivor has an arrest or conviction record, is or has been incarcerated, or is or has been under any form of correctional supervision.\n**(E)**\nAny allegation that the survivor contributed to the survivor\u2019s own victimization.\n**(F)**\nThe identity of the person who committed the act of the violence (including whether the person is a law enforcement officer) or the relationship of the person to the victim.\n#### 3. Flexible assistance for survivors of violence\n##### (a) Grant program established\nThe Attorney General, acting through the Director of the Office for Victims of Crime of the Department of Justice (in this section referred to as the Director ), is authorized to award grants to community-based organizations for the purpose of establishing assistance funds to distribute direct cash assistance to survivors of violence, with the goal of improving safety, healing, and financial stability for survivors of violence, and family members of survivors of violence.\n##### (b) Application\nAn eligible community-based organization seeking a grant under this section shall submit an application at such time, in such manner, and containing such information as the Director may reasonably require, including the following:\n**(1)**\nA description of the organization\u2019s history serving one or more of the groups described in subsection (e)(4).\n**(2)**\nA description of how the community or communities the organization serves are impacted by violence and incarceration.\n**(3)**\nThe estimated number of survivors of violence or family members of survivors of violence the organization currently serves.\n**(4)**\nThe estimated number of survivors of violence or family members of survivors of violence to whom the organization anticipates it will distribute grant funds.\n**(5)**\nHow the organization plans to distribute cash assistance to survivors of violence or family members of survivors of violence to meet their immediate financial needs.\n**(6)**\nHow the organization plans to minimize the burden on survivors of violence and their family members to provide excessive documentation or paperwork.\n##### (c) Eligibility\nA community-based organization shall be eligible to apply for a grant under this section if the organization has a history of serving survivors of violence, and the majority of people the organization, or a project within the organization that will administer the grant, serves are survivors of violence.\n##### (d) Administration\nIn administering the grant program under this section, the Director shall do all of the following:\n**(1)**\nStrive to minimize the paperwork burden on grant applicants and grantees.\n**(2)**\nStrive to develop application, awards, and reporting processes that are accessible to community-based organizations without past experience receiving a Federal grant award.\n**(3)**\nDevelop a plan to publicize the grant program in advance of an application deadline.\n**(4)**\nProvide technical assistance and training opportunities to applicants and grantees.\n**(5)**\nDevelop tools to support applicants applying for a grant under this section, including, templates and sample applications, which shall be posted prominently on the website of the Office for Victims of Crimes.\n**(6)**\nDevelop a website where survivors of violence and members of the public can locate contact information for community-based organizations receiving grants under this section.\n##### (e) Priority\nWhen considering grant applications, the Director shall give priority to community-based organizations that\u2014\n**(1)**\nare located in, serve, and directly employ members of communities that experience disproportionately high rates of gun violence and imprisonment, as compared to such rates nationally, as evidenced by, during the prior 3-year period\u2014\n**(A)**\ndisproportionately high rates of individuals who have been injured or killed by a firearm, as compared to such rates nationally; and\n**(B)**\ndisproportionately high rates of individuals who have been arrested or sent to jail or prison, as compared to such rates nationally;\n**(2)**\nare led by, or employ, individuals who are survivors of violence or who are formerly incarcerated;\n**(3)**\nare led by individuals who have proven ties to the community in which the organization operates;\n**(4)**\nhave a history of providing services focusing on vulnerable survivors of violence, including\u2014\n**(A)**\nsurvivors of color;\n**(B)**\nsurvivors with disabilities;\n**(C)**\nsurvivors who are transgender or gender nonconforming;\n**(D)**\nsurvivors who have faced disproportionate police contact;\n**(E)**\nsurvivors who are formerly incarcerated or who have past arrests or convictions;\n**(F)**\nimmigrant survivors;\n**(G)**\nNative American survivors;\n**(H)**\nsurvivors who are unhoused;\n**(I)**\nsurvivors of firearm injuries;\n**(J)**\nsurvivors who have lost a family member to homicide;\n**(K)**\nlow-income survivors; or\n**(L)**\ngeographically underserved survivors; and\n**(5)**\nhave leadership that reflects the racial and ethnic diversity of the community in which the organization operates.\n##### (f) Geographic diversity\nIn selecting grant recipients, the Director shall ensure that, collectively, grantees represent a diversity of geographic areas.\n##### (g) Use of funds\n**(1) Distribution of funds**\nAn organization receiving a grant under this section may use the funds as follows:\n**(A)**\nDistributing unrestricted cash assistance to survivors of violence to meet the financial needs of survivors or to cover the expenses of survivors, which assistance\u2014\n**(i)**\nmay be distributed at the discretion of the organization and in amounts determined by the organization based on the needs of survivors, and in a way that minimizes or eliminates the burden on survivors to provide external documentation of their needs or expenses;\n**(ii)**\nmay be distributed directly to a survivor, to the parent or guardian of a survivor if the survivor is a minor or dependent adult, or if the survivor or the parent or guardian of a minor or dependent survivor requests, to a vendor, business, or another third party to pay for an expense or purchase a product on a survivor\u2019s behalf; or\n**(iii)**\nmay be distributed in the form of cash, electronic transfer, check, direct deposit, prepaid card, or in another similar manner at the discretion of the organization and based on the needs of survivors.\n**(B)**\nTo establish and maintain a program to distribute the assistance described under subparagraph (A), including staffing, training, operational, and evaluation expenses, except that not more than 20 percent of the grant may be used for the purposes under this subparagraph.\n**(2) Policies and procedures**\nA community-based organization receiving a grant under this section shall establish and maintain policies and procedures for distributing cash assistance to survivors of violence that\u2014\n**(A)**\npromote the distribution of cash assistance to survivors in a manner that meets the immediate needs of survivors quickly;\n**(B)**\ndo not require survivors to engage in other services or programs as a condition of receiving cash assistance;\n**(C)**\ndo not require survivors to provide or maintain burdensome documentation of their need or spending;\n**(D)**\ndo not require survivors to report a crime to a law enforcement agency, court, or other local, State, Tribal, or Federal agency designated to investigate or prosecute crimes, abuse, or violence as a condition of receiving cash assistance;\n**(E)**\ndo not exclude survivors on the basis of citizenship or immigration status; and\n**(F)**\ndo not exclude survivors on the basis of an arrest or conviction record, nor on the basis of a survivor\u2019s status under correctional control or supervision.\n##### (h) Grant duration\nA grant awarded under this section shall be for a 4-year period.\n##### (i) First award\nSubject to the availability of appropriations, not later than 9 months after the date of enactment of this Act, the Director shall make the first grant award under this section.\n##### (j) Exclusion from income, resources, and assets\n**(1) Flexible cash assistance payments excluded from income, resources, and assets for purposes of means tests**\nNotwithstanding any other provision of law (other than section 1403 of the Victims of Crime Act of 1984 ( 34 U.S.C. 20102 )), for the purpose of any maximum allowed income, resource, or asset eligibility requirement in any Federal, State, or local government program using Federal funds that provides medical or other assistance (or payment or reimbursement of the cost of such assistance), any amount of cash assistance received by a survivor of violence through the grant program established under this section shall not be included for purposes of calculating income, resources, or assets of the survivor, nor shall that amount reduce the amount of the assistance available to the survivor from Federal, State, or local government programs using Federal funds.\n**(2) Flexible cash assistance payments not considered gross income**\nNotwithstanding any other provision of law, any cash assistance received by a survivor of violence through the grant program established under this section shall be excluded from gross income under section 61 of the Internal Revenue Code of 1986.\n##### (k) Reports\n**(1) Reports to the Director**\nNot later than 1 year after receiving a grant under this section, and annually thereafter, each community-based organization that receives a grant under this section shall submit a report on the use of such grant funds to the Director, as required by the Director. Such report shall, at a minimum, include\u2014\n**(A)**\nthe aggregate number of survivors of violence who received cash assistance through the grant program; and\n**(B)**\nthe average amount of assistance each such survivor received through the grant program.\n**(2) Report to Congress**\nNot later than 1 year after the date on which the first 4-year grant period under this section ends, and every 4 years thereafter, the Director shall submit to Congress a report that, at a minimum, includes\u2014\n**(A)**\nany findings resulting from reports submitted to the Director under paragraph (1); and\n**(B)**\nbest practices for grantees under this section to implement flexible cash assistance programs for survivors of violence.\n##### (l) Administration and evaluation\nThe Director may reserve up to 8 percent of the funds appropriated for the grant program each year for the costs of administering the grant program, including, without limitation, employing personnel, providing technical assistance or training to grantees or prospective grantees, contracting with independent researchers to evaluate the impact of the program, and issuing a report on the impact of the grant program.\n##### (m) Authorization of appropriations\nThere is authorized to be appropriated to implement this section $40,000,000 for each of fiscal years 2027 through 2031.\n#### 4. State level supplemental victim surveys\n##### (a) In general\nNot later than one year after the date of enactment of this Act, the Attorney General, acting through the Director of the Bureau of Justice Statistics of the Department of Justice (in this section referred to as the Director ), shall make grants to States to administer surveys to survivors of violence to determine their needs related to having been survivors of violence.\n##### (b) Priority\nThe Director shall prioritize awarding grants to recipients that solicit information about one or more of the following:\n**(1)**\nThe types of services survivors of violence received related to having been victimized, and the experiences of such survivors while receiving such services.\n**(2)**\nWhether survivors wanted services that they did not receive.\n**(3)**\nThe experiences of survivors with relocation, eviction, immigration, and housing following victimization.\n**(4)**\nThe experiences of survivors with the use of force by and injury caused by law enforcement officers.\n**(5)**\nThe prevalence of victimization and the post-victimization needs of\u2014\n**(A)**\nindividuals who have been arrested or convicted of crimes;\n**(B)**\nindividuals who are unhoused; or\n**(C)**\nindividuals who are living in institutions, including prisons, jails, medical or nursing facilities, or mental health facilities.\n##### (c) Reports\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, and annually thereafter, each State that receives a grant under this section shall submit to the Director a report documenting the results and findings from the survey funded by the grant.\n**(2) Publication by Director**\nThe Director shall make publicly available on the website of the Bureau of Justice Statistics the reports submitted under paragraph (1).\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $5,000,000 for each of fiscal years 2027 and 2031.\n#### 5. Definitions\nIn this Act:\n**(1) Community-based organization**\nThe term community-based organization means a nonprofit, nongovernmental, or Tribal organization that serves a specific geographic community. Such term does not include any law enforcement agency or any court, or any other local, State, or Federal agency designated to investigate or prosecute crimes, abuse, or violence.\n**(2) Family member**\n**(A) In general**\nExcept as provided in subparagraph (B), the term family member means, with respect to an individual, any of the following:\n**(i)**\nA child (whether a biological, foster, adoptive, or step relationship), or a person who is under the legal guardianship of the individual or to whom the individual stands in loco parentis or has stood in loco parentis.\n**(ii)**\nA biological, adoptive, or foster parent, stepparent, or legal guardian of an individual or an individual\u2019s spouse or domestic partner, or a person who stood in loco parentis when the individual or the individual\u2019s spouse or domestic partner was a minor child.\n**(iii)**\nA person to whom the individual is legally married under the laws of any State, or a domestic partner.\n**(iv)**\nA grandparent, grandchild, or sibling (whether a biological, foster, adoptive, or step relationship) of the individual or of the individual\u2019s spouse or domestic partner.\n**(v)**\nA person who lives in the same household as the individual.\n**(vi)**\nAny other individual related by blood, adoption, or marriage or whose close association with the individual is the equivalent of a family relationship.\n**(B) Exclusion**\nSuch term does not include a person who has committed an act or conduct described in clause (i) through (vi) of subparagraph (A) against the individual.\n**(3) Survivor of violence**\nThe terms survivor of violence means an individual against whom any of the following have been committed:\n**(A)**\nAn act or conduct during which another person\u2014\n**(i)**\ncaused or threatened to cause bodily injury to that individual;\n**(ii)**\nexhibited, drew, brandished, or used a firearm, or other weapon, against that individual; or\n**(iii)**\nused, or threatened to use, force against that individual to cause injury or death.\n**(B)**\nDating violence.\n**(C)**\nDomestic violence.\n**(D)**\nFamily violence.\n**(E)**\nSexual assault.\n**(F)**\nSexual harassment.\n**(G)**\nTrafficking.\n**(H)**\nStalking.\n**(4) Tribal organization**\nThe term Tribal organization has the meaning given such term in section 40002 of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291 ).",
      "versionDate": "2026-04-21",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-01T18:34:48Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8426ih.xml"
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
      "title": "Crime Survivor Support and Stability Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-25T04:38:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Crime Survivor Support and Stability Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-25T04:38:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To encourage States to provide rights to survivors of violence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-25T04:33:34Z"
    }
  ]
}
```
