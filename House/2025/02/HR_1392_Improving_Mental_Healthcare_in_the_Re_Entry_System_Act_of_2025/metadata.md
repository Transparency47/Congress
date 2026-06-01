# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1392?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1392
- Title: Improving Mental Healthcare in the Re-Entry System Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1392
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-07-08T13:02:21Z
- Update date including text: 2025-07-08T13:02:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1392",
    "number": "1392",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001207",
        "district": "11",
        "firstName": "Mikie",
        "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
        "lastName": "Sherrill",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Improving Mental Healthcare in the Re-Entry System Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-08T13:02:21Z",
    "updateDateIncludingText": "2025-07-08T13:02:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:32:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1392ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1392\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Ms. Sherrill introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide funding to the Bureau of Prisons, States, and localities to carry out mental health screenings and provide referrals to mental healthcare providers for individuals in prison or jail.\n#### 1. Short title\nThis Act may be cited as the Improving Mental Healthcare in the Re-Entry System Act of 2025 .\n#### 2. Grant program\n##### (a) Establishment\nNot later than 90 days after the date of the enactment of this Act, the Attorney General shall establish a grant program (hereinafter referred to as the Program ) to implement and administer mental health screenings to individuals at intake into an eligible detention center and refer such individuals to mental healthcare providers before or immediately after exit from an eligible detention center, as applicable.\n##### (b) Grant authority\nIn carrying out the Program, the Attorney General may award a grant on a competitive basis to an eligible recipient in accordance with this section.\n##### (c) Application\nThe Attorney General may award a grant under the Program to a State or locality, determined by the Attorney General to carry out a project described in subsection (d).\n##### (d) Eligible recipients\n**(1) Hiring requirement**\nTo be eligible for a grant under the Program, a State or locality shall hire a mental health liaison staff member for each eligible detention center under its jurisdiction. If an eligible detention center has a small enough population, subject to approval by the Advisory Board, one mental health liaison staff member may cover multiple detention centers. The mental health liaison staff member shall be responsible for\u2014\n**(A)**\ncoordinating efforts between the prison or jail and mental health providers in the local region to help individuals currently or formerly in prison or jail access mental healthcare;\n**(B)**\ncoordinating with the Advisory Board to ensure that the Program is operating in accordance with this section; and\n**(C)**\noverseeing and coordinating activities of the outreach team (as described in subsection (g)).\n**(2) Plan**\nTo be eligible for a grant under the Program, a State or locality shall submit a plan to the Advisory Board explaining how the Program established shall meet the criteria under subsection (e).\n**(3) Relevant data**\nTo be eligible for a grant under the Program, a State or locality shall partner with the Advisory Board and an independent research organization to evaluate the impact of their program as a condition of receiving a grant, and are also required to share relevant data with the Advisory Board and the research organization contracted with by the Attorney General as specified by section 5(a) regarding individuals\u2019 participation in the mental health screen and referral program and their arrest, arraignment, and incarceration rates.\n##### (e) Eligible projects\nGrant funds awarded under the Program may only be used to:\n**(1)**\nDevelop and administer a brief mental health screening survey as required under subsection (f).\n**(2)**\nDevelop any technology necessary for a prison or jail to provide the survey under paragraph (1).\n**(3)**\nHire any staff necessary for a prison or jail to provide the survey under paragraph (1).\n**(4)**\nEstablish an outreach team pursuant to subsection (g) to refer an individual, if their responses to the survey indicate severe mental illness, to a local mental healthcare provider for further assessment and outreach, admission (when necessary), and support for that individual in re-establishing ties with a mental health provider.\n**(5)**\nPay the salary or overtime pay of an outreach team as established pursuant to subsection (g), including providing direct funding to a prison, jail, or mental health center to compensate staff members.\n##### (f) Brief mental health screening survey\nThe mental health screening survey developed and administered under subsection (e) shall:\n**(1)**\nBe composed of 5 to 10 questions.\n**(2)**\nBe based on the questions and content of the Brief Jail Mental Health Screen (BJMHS).\n**(3)**\nSeek to identify severe mental illnesses, including schizophrenia, bipolar disorder, and major depression.\n**(4)**\nAsk individuals about the symptoms of severe mental illness they may be experiencing or have experienced and any prior use of mental health-related medications or inpatient care.\n**(5)**\nIdentify the individual\u2019s place of residence.\n**(6)**\nBe administered by a trained staff member at the jail or prison to all entering individuals who are incarcerated in the jail or prison and to all incarcerated individuals who entered the jail or prison before the survey was implemented.\n##### (g) Outreach team\n**(1) In general**\nA referral to a mental healthcare provider, as described in subsection (e), shall be made by a mental health outreach team that is composed of\u2014\n**(A)**\nmental healthcare professionals and clinicians from mental healthcare centers local to the prison or jail;\n**(B)**\nstaff from the jail or prison, when applicable; and\n**(C)**\na mental health liaison staff member who shall oversee the outreach team.\n**(2) Alert**\nIf an individual has been determined to need a referral to a mental healthcare provider, the mental health outreach team shall be notified immediately by jail or prison staff and informed, when applicable, of the individual\u2019s release date from such jail or prison and the individual\u2019s trial date.\n**(3) Contact attempts required**\n**(A) In general**\nA mental health outreach team member shall first attempt to contact an individual that has been determined to need a referral to a mental healthcare provider in person at the jail or prison, before such individual is released. If in person contact was not made before such individual was released from prison or jail, the outreach team member shall attempt to contact via telephone such individual within 24 hours, and at the latest within 48 hours, of their release from jail or prison for the purpose of making the mental health referral. The mental health outreach team member shall not need to contact the individual via telephone after release if such contact was made in person.\n**(B) Additional contacts**\nA mental health outreach team member shall make at least three attempts at telephone contact for each individual that has been determined to need a referral to a mental healthcare provider if in person contact before release was not made. If phone contact is unsuccessful, a mental health outreach team member shall attempt to contact the individual in person at their place of residence, as provided on the mental health survey.\n#### 3. Bureau of Prisons\nNot later than 90 days after the date of the enactment of this Act, the Director of the Bureau of Prisons shall establish a program that is substantially similar to the Program established under section 2 to implement and administer mental health screenings to individuals at intake into an eligible detention center and refer such individuals to mental healthcare providers before or immediately after exit from an eligible detention center, as applicable.\n#### 4. Advisory board on program implementation\n##### (a) Establishment\nNot later than 60 days after the date of the enactment of this Act, the Attorney General shall establish an Advisory Board to manage and administer the Program under section 2, with the responsibility to:\n**(1)**\nEvaluate and approve the plans submitted by a State or locality as required under section 2 and to ensure that grant funding is used as specified under section 2.\n**(2)**\nMonitor plans submitted by the Bureau of Prisons and advise the Attorney General on compliance to ensure that funding to the Bureau of Prisons is used as specified under section 2.\n**(3)**\nProvide technical assistance to a State or locality to help with the implementation and administration of mental health screening and referral programs that maximize impact on reducing crime rates and improving employment and wage rates for individuals released from prison or jail, and to assist a State or locality\u2019s coordination with the Attorney General in implementing the Program.\n**(4)**\nPublish a database of completed evaluations of the impact of a Program, as specified under section 5.\n**(5)**\nCreate a working group of mental healthcare providers, jail and prison administrators, law enforcement officials, and operators of existing mental health screening and referral programs, as of the creation of the working group, to share best practices on how to create and implement mental health screening and referral programs that have the largest impact on reducing crime rates and improving employment and wage rates for individuals released from prison or jail.\n**(6)**\nWork in coordination with mental health outreach teams as established under section 2, to ensure that the Program is operating as required.\n**(7)**\nDetermine if a grant awarded by the Program is not meeting the requirements of the Program and mandate necessary changes and reduce funding if such changes are not made.\n**(8)**\nOversee the completion of required program evaluations as described under section 5, by\u2014\n**(A)**\ncontracting with one or more independent research organizations to carry out an evaluation of the impact of each grant awarded under the Program on arrest, arraignment, and incarceration rates, employment and wage rates, and mental healthcare utilization rates of individuals who have been administered mental health screening; and\n**(B)**\nworking with the Bureau of Prisons, States, and localities to ensure that the evaluation is successfully completed.\n##### (b) Technical assistance\nThe Advisory Board shall provide technical assistance to the Bureau of Prisons, States, and localities in setting up and administering the Program and shall identify evidence-backed models for the administration of mental health screening and referral programs that the Bureau of Prisons, States, and localities can look to when designing their own programs.\n##### (c) Process evaluation activities\nNot later than one year after the Program begins, the Advisory Board shall conduct a process evaluation for a grant awarded under the Program, in which the implementation of the surveys and referrals in each prison or jail is monitored and evaluated to ensure that they are being carried out as specified in the plan submitted to the Advisory Board.\n##### (d) Membership\n**(1) In general**\nThe Attorney General shall appoint members to serve on the Advisory Board established under subsection (a) who have expertise with respect to\u2014\n**(A)**\ndesigning and administering mental health screenings and providing referrals for those incarcerated in prisons or jails, or for those who have recently left such facilities;\n**(B)**\nmental healthcare within prisons or jails; or\n**(C)**\nprogram evaluation using rigorous experimental and quasi-experimental statistical methods.\n**(2) Number of members**\nThe Attorney General shall appoint as many members to the Advisory Board established under subsection (a) as deemed necessary by the Attorney General.\n#### 5. Evaluation activities\n##### (a) Independent research organizations\nThe Attorney General shall provide funding directly to the Advisory Board for the purpose of contracting with one or more independent research organizations, in partnership with the Bureau of Prisons, States, and localities, to carry out an evaluation to determine whether each grant awarded under the Program is being implemented effectively and to measure the impact of such programs.\n##### (b) Impact evaluation activities\n**(1) In general**\nNot later than one year after a recipient of a grant awarded under the Program receives an award they shall conduct an impact evaluation for its program, in which the surveys and referrals in each prison or jail will be evaluated for their effect on the criminal justice and economic outcomes of individuals who receive the survey. Such impact evaluation shall be conducted by an independent research organization, with oversight from the Advisory Board and include an analysis of the impact of the survey and referral on participant crime rates, including arrest, arraignment, and incarceration rates, participant employment and wage rates, and participant mental healthcare utilization rates for one year, three years, five years, and ten years after the participant has completed the survey and referral program. These analyses will use administrative data collected by each State\u2019s department of public safety, for the crime rate data, and each State\u2019s Department of Labor, for the employment and wage rate data. States shall provide this data to the independent research organization. For the mental health utilization data, data from mental health providers and, if necessary, from outreach to the individuals who participated in the survey and referral program shall be utilized.\n**(2) Experimental design**\nProgram impact evaluations under paragraph (1) shall use randomized control experimental or quasi-experimental research designs. Randomized control experimental designs are preferred and the Advisory Board will provide the independent research organization, in partnership with the Bureau of Prisons, State, or Locality, additional resources to carry out a randomized control experimental evaluation.\n##### (c) Database\nOnce evaluations become available, the Advisory Board will be required to keep an updated database of the impact of programs funded under the grant program and how those programs were implemented and administered, with the goal of creating a repository of evidence regarding what drives impact on crime rates and employment and wage rates to guide policymakers and program operators in the future.\n#### 6. Funding\n##### (a) Authorization\nThere is authorized to be appropriated to the Attorney General to carry out this Act\u2014\n**(1)**\n$100,000,000 for fiscal year 2026;\n**(2)**\n$110,000,000 for fiscal year 2027;\n**(3)**\n$120,000,000 for fiscal year 2028;\n**(4)**\n$130,000,000 for fiscal year 2029; and\n**(5)**\n$140,000,000 for fiscal year 2030.\n##### (b) Distribution of funds\nOf the amounts made available under subsection (a), the Attorney General shall use\u2014\n**(1)**\n90 percent of such amount for a grant program under sections 2 and 3, as applicable, of which\u2014\n**(A)**\n20 percent shall go to the Bureau of Prisons for screening and referral implementation activities at Federal prisons;\n**(B)**\n20 percent shall go to States as competitive grants to carry out screening and referral implementation activities at State prisons; and\n**(C)**\n50 percent shall go to localities as competitive grants to carry out screening and referral implementation activities at locally-administered jails;\n**(2)**\n5 percent of such amount to carry out evaluation activities under section 5; and\n**(3)**\n5 percent of such amount for the Advisory Board to provide technical assistance to the Bureau of Prisons, States, and localities and for general operations as described in section 4.\n#### 7. Definitions\nIn this Act:\n**(1) State**\nThe term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n**(2) Locality**\nThe term locality means any city, county, township, town, borough, parish, village, or other general purpose political subdivision of a State.\n**(3) Mental healthcare provider**\nThe term mental healthcare provider means a fully-licensed professional or group of professionals who diagnose mental health conditions and provide mental health treatment, and who operate near to the relevant jail or prison. Mental healthcare providers may provide services at hospitals or at private clinics.\n**(4) Mental healthcare center**\nThe term mental healthcare center means any facility where one or more mental healthcare providers offer mental health services, such as a hospital or private clinic.\n**(5) Jail or prison administrator**\nThe term jail or prison administrator means any individual who has been appointed to a supervisory position in a Federal, State, or local incarceration facility by the Federal Government, a State, or a locality.\n**(6) Law enforcement official**\nThe term law enforcement official means any officer of an entity administered by a locality, State, or the Federal Government that exists primarily to prevent and detect crime and enforce criminal laws who is designated by the leadership of that entity to represent the entity.\n**(7) Eligible detention center**\nThe term eligible detention center means any prison or jail administered by the Bureau of Prisons or a State or any jail administered by a State or locality.\n**(8) Severe mental illness**\nThe term severe mental illness means one or more mental, behavioral, or emotional disorders that results in serious functional impairment and substantially interferes with or limits major life activities.\n**(9) Independent research organizations**\nThe term independent research organization means an entity that is not operated or controlled by a governmental body that conducts high-quality and rigorous experimental and quasi-experimental evaluations.\n**(10) Randomized control experimental research design**\nThe term randomized control experimental research design means a study design that utilizes a randomized control trial methodology to determine the impact of the program on participants, by comparing program outcomes between a randomly assigned sample population that has received the survey and referral and a randomly assigned control population that has not received the survey and referral.\n**(11) Responses to the survey indicate severe mental illness**\nThe term responses to the survey indicate severe mental illness means an individual answer\u2019s yes to multiple questions with respect to the symptoms of a severe mental illness or to any question relating to prior use of a mental health-related medication or inpatient care related to a mental illness.\n**(12) Quasi-experimental research design**\nThe term quasi-experimental research design means a study design that utilizes a non-randomized methodology and model to determine the impact of the program on participants, by comparing program outcomes between a non-randomly assigned sample population that has received the survey and referral and a non-randomly assigned control population that is constructed to be statistically identical to the sample population but without having received the survey and referral.",
      "versionDate": "2025-02-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-07-08T13:02:05Z"
          },
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-07-08T13:01:27Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-07-08T13:01:44Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-07-08T13:01:51Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-08T13:02:15Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-08T13:02:02Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-07-08T13:01:56Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-07-08T13:01:37Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-07-08T13:01:31Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-07-08T13:02:21Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-08T13:02:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-14T11:55:01Z"
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
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1392ih.xml"
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
      "title": "Improving Mental Healthcare in the Re-Entry System Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Mental Healthcare in the Re-Entry System Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide funding to the Bureau of Prisons, States, and localities to carry out mental health screenings and provide referrals to mental healthcare providers for individuals in prison or jail.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:18:34Z"
    }
  ]
}
```
