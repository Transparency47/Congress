# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5538?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5538
- Title: Child Rescue Act
- Congress: 119
- Bill type: HR
- Bill number: 5538
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2025-12-15T20:08:43Z
- Update date including text: 2025-12-15T20:08:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5538",
    "number": "5538",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Child Rescue Act",
    "type": "HR",
    "updateDate": "2025-12-15T20:08:43Z",
    "updateDateIncludingText": "2025-12-15T20:08:43Z"
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
          "date": "2025-09-19T13:05:10Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5538ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5538\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mr. Vindman (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to convene a national working group to study proactive strategies and needed resources for the identification and rescue of children from sexual exploitation and abuse, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Child Rescue Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe growing international trade in child sexual abuse material creates demand and incentive for the sexual assault of children throughout the United States.\n**(2)**\nUnited States law enforcement efforts to combat child sexual exploitation have the potential to help multiple distinct groups of victims, including\u2014\n**(A)**\nchildren depicted in child sexual abuse material (CSAM) who are still being abused;\n**(B)**\nchildren and adults whose victimization as a child continues to be viewed and shared online; and\n**(C)**\nchildren who are being sexually abused or exploited by adults who could be interdicted while accessing or sharing CSAM online.\n**(3)**\nIn 2021, law enforcement investigative systems detected more than 325,000 unique Internet Protocol addresses in the United States seen distributing child sexual abuse material across peer-to-peer file sharing networks.\n**(4)**\nA growing body of research, including academic studies, analysis by the United States Sentencing Commission, and findings by law enforcement polygraphers, indicates that a significant percentage of majority of individuals possessing and sharing CSAM are dual offenders who possess illegal imagery and also commit contact offenses. In 2021, the United States Sentencing Commission found that in fiscal year 2019, 48 percent of non-production child pornography offenders engaged in aggravating sexual conduct prior to, or concurrently with , their current offense. Studies including Seto et al, the Butner Redux, the OJJDP study, and Bourke et al Tactical Polygraph study have found that between 50 and 80 percent of offenders who possess CSAM are also committing contact sexual offenses against children.\n**(5)**\nAccording to a 2018 study by the National Center for Missing and Exploited Children (NCMEC), in cases involving a single victim and single offender, actively traded cases were associated with having prepubescent victims. Actively traded cases were also associated with more egregious content in terms of sexual activity, and more likely to involve familial offenders, particularly nuclear family members .\n**(6)**\nCyberTipline reports often lead to the rescue of children through the successful investigation of offenders who are not only exploiting children by circulating CSAM, but who are also committing contact offenses. In 2020, 21,700,000 CyberTipline reports were submitted to NCMEC and approximately 288,000 CyberTipline reports were made available to the 61 Internet Crimes Against Children (ICAC) units across the country.\n**(7)**\nUnited States law enforcement\u2019s ability to detect and interdict online traffic in CSAM provides an opportunity to locate sexual predators and rescue children through victim-centric investigations.\n**(8)**\nWith inadequate resources, United States law enforcement agencies are increasingly unable to adequately respond to this rapidly growing number of CyberTips and other investigative leads, a problem which also reduces the number of proactive undercover investigations and education activities they can conduct.\n**(9)**\nInvestigations of these crimes are complicated by the increasing prevalence of encryption and anonymizing services available to offenders.\n#### 3. United States Working Group on Children in Imminent Danger of Sexual Abuse and Exploitation\n##### (a) Establishment\nNot later than 90 days after the date of the enactment of this Act, the Attorney General shall establish a national working group, to be known as the United States Working Group on Children in Imminent Danger of Sexual Abuse and Exploitation (hereinafter referred to as the Working Group ), to study victim-centric policing strategies and resource needs to identify and rescue\u2014\n**(1)**\nchildren in the United States who are visually depicted in child sexual abuse material;\n**(2)**\nchildren in the United States who are victims of sexual abuse by individuals who are engaged in an offense relating to child sexual abuse materials; and\n**(3)**\nchildren located outside the United States who are visually depicted in child sexual abuse materials where the perpetrators are in the United States.\n##### (b) Duties of the working group\n**(1) Information request**\nNot later than 30 days after the establishment of the Working Group under subsection (a), the Working Group shall solicit from each State, Tribal, or local law enforcement agency the information necessary to develop the estimates under paragraph (2).\n**(2) Development of estimates**\nThe Working Group shall:\n**(A)**\nDevelop estimates of the total number of individuals suspected with respect to child sexual abuse material or other crimes involving sexual contact with children in the United States, including those who are\u2014\n**(i)**\nknown to a law enforcement agency;\n**(ii)**\nidentified by law enforcement through proactive policing; or\n**(iii)**\nreported to the CyberTipline of NCMEC (or any successor to the CyberTipline operated by NCMEC).\n**(B)**\nDevelop estimates of the total number of child victims of child sexual abuse in the United States who could be located and protected from further abuse through the apprehension of suspects described under subparagraph (A).\n**(C)**\nDevelop recommendations of the funding, resources, and proactive and reactive strategies necessary for law enforcement agencies to successfully identify, locate, and protect child victims\u2014\n**(i)**\ndescribed in subparagraph (B); and\n**(ii)**\nwho appear in child sexual abuse material known to a law enforcement agency or NCMEC.\n**(D)**\nDevelop or obtain estimates of the number of child sexual abuse reports made annually to law enforcement agencies and to State, Tribal, and local child protective services, broken out by locality and relationship between victim and offender, including adults in a position of trust or authority.\n**(E)**\nDevelop recommendations for strategies, best practices, and resources that could be used by law enforcement agencies to determine whether offenders alleged to have committed a crime involving sexual contact should also be investigated for potential child sexual abuse material crimes.\n**(F)**\nDevelop recommendations of victim-centric and proactive policing strategies, international collaboration, and resource needs to apprehend offenders in the United States who are engaged in offenses related to children as described in subsection (a)(3).\n**(G)**\nDevelop estimates of, or compile data solicited under paragraph (1)\u2014\n**(i)**\nthe number of adults who were arrested by law enforcement agencies during the 5-year period preceding the date of enactment of this Act, by year, for offenses or violations described in subparagraphs (A) through (D);\n**(ii)**\nthe number of adults who were prosecuted at the State, Tribal, or Federal level during the 5-year period preceding the date of the enactment of the Act, by year, for offenses described in subparagraphs (A) through (D); and\n**(iii)**\nthe number of children who are unidentified victims of child sexual abuse material described in subparagraph (C)(ii).\n**(H)**\nAnalyze and summarize common reasons why investigations of reports of child sexual abuse or exploitation do not go forward.\n**(I)**\nDevelop guidance for Internet Crimes Against Children Task Forces to adopt a prioritization framework with respect to the investigation and prosecution of all child sexual abuse and exploitation, including prioritizing investigating individuals using encryption or anonymization.\n**(J)**\nDevelop guidance on the Attorney General\u2019s response to technology companies that refuse to comply with lawful requests for information related to offenders who use virtual private networks.\n**(K)**\nEvaluate the current duties and responsibilities of ICAC Task Forces pursuant to section 21114 of title 34, United States Code, including on\u2014\n**(i)**\nworkloads; and\n**(ii)**\ntheir ability to pursue investigations which are most likely to result in the identification of offenders described in subparagraph (A) and children described in subparagraph (B).\n**(3) Report**\n**(A) In general**\nNot later than 365 days after the date of enactment of this Act, the Working Group shall submit to the Attorney General, the Committee on the Judiciary of the Senate, the Committee on Appropriations of the Senate, the Committee on the Judiciary of the House of Representatives, and the Committee on Appropriations of the House of Representatives, a report that contains\u2014\n**(i)**\na detailed statement of the findings and conclusions of the Working Group, together with recommendations for legislation; and\n**(ii)**\na summary of the support, documents, and witnesses provided by the Attorney General to the Working Group.\n**(B) Material included**\nA majority vote of the members of the Working Group shall determine the findings, conclusions, and recommendations included in the report submitted under subparagraph (A).\n**(C) Documentation of numerical edits**\nIf for any reason the Working Group is unable to develop the estimates under paragraph (2), the Working Group shall in the report under this paragraph document the reasons such estimates could not be developed and make recommendations toward developing such estimates.\n##### (c) Members of the Working Group\n**(1) In general**\n**(A) Attorney General discretion**\nThe Working Group shall be composed of representatives of Federal departments and agencies, law enforcement agencies, Tribal governmental agencies, nongovernmental organizations, and other subject matter experts as the Attorney General determines appropriate.\n**(B) Specified members**\nThe Attorney General shall appoint representatives of the following agencies and nongovernmental organizations to the Working Group:\n**(i)**\nThree representatives from State or unit of local government who have received a grant from the Internet Crimes Against Children Task Force program with extensive, direct experience conducting both CyberTipline investigations and proactive, online undercover investigations, including the use of specialized tools for peer-to-peer investigations.\n**(ii)**\nThe Chief or Deputy Chief of the Child Exploitation and Obscenity Section of the Criminal Division of the Department of Justice.\n**(iii)**\nThe National Coordinator for Child Exploitation Prevention and Interdiction of the Department of Justice.\n**(iv)**\nA representative of the Behavioral Analysis Unit of the United States Marshals Service with subject matter expertise in child exploitation offenders who also commit contact offenses.\n**(v)**\nA special agent of Homeland Security Investigations with expertise in both CyberTipline investigations and proactive online investigations.\n**(vi)**\nA subject matter expert within Homeland Security Investigations with expertise in child victim identification.\n**(vii)**\nA special agent of the Federal Bureau of Investigation with expertise in both CyberTipline investigations and proactive online investigations and the use of polygraphs in child sexual abuse material investigations.\n**(viii)**\nA representative from the National Children\u2019s Alliance with expertise in child exploitation and child victim forensic interviewing.\n**(ix)**\nA special agent of the United States Secret Service with expertise in investigations of child sexual abuse material or polygraphs of child sexual exploitation suspects.\n**(x)**\nA Postal Inspector at the United States Postal Inspection Service with expertise in child sexual abuse material investigations.\n**(xi)**\nA representative from the National District Attorney\u2019s Association.\n**(xii)**\nA representative from the academic community with expertise in developing technology that can proactively detect the distribution of child sexual abuse material online.\n**(xiii)**\nA representative of the Office of Juvenile Justice and Delinquency Prevention with expertise in available data sources and methods for developing prevalence estimates using direct and indirect methods of estimation.\n**(xiv)**\nA representative of the Executive Office of the United States Attorney.\n**(xv)**\nA recently retired Internet Crimes Against Children Task Force Commander.\n**(xvi)**\nA representative from National Child Protection Task Force.\n**(xvii)**\nRepresentatives from the Department of Justice Office of Tribal Justice and the Bureau of Indian Affairs Office of Justice Services.\n**(xviii)**\nA representative of the Rape, Abuse & Incest National Network with subject matter expertise on child sexual exploitation and abuse.\n**(xix)**\nA representative of the International Justice Mission with subject matter expertise on cross-border, live-streamed child sexual abuse.\n**(C) Technical assistance**\nThe Working Group shall establish a Technical Assistance Board to provide guidance and technical assistance to the Working Group, composed of the following:\n**(i)**\nA representative from the ICAC Child Online Protection System (ICACCOPS) at the National Criminal Justice Training Center with subject matter expertise on child sexual exploitation and abuse investigations.\n**(ii)**\nA representative from the Child Rescue Coalition with subject matter expertise on the Child Protection System and other child sexual exploitation and abuse investigations.\n**(iii)**\nA representative from the National Center for Missing and Exploited Children with subject matter expertise on child sexual exploitation and abuse and child victim identification.\nThe Working Group shall consult with the members of the Technical Assistance Board throughout the execution of its duties under subsection (b). Representatives of the Technical Assistance Board under paragraph (1) from each organization shall have the right to be present at each Working Group meeting.\n**(2) Cessation of membership**\nIf an individual is appointed to the Working Group based on membership in an agency or organization and the individual ceases to be a member of that agency or organization, the individual shall cease to be a member of the Working Group on the date on which the member ceases to be a member of the agency or organization.\n**(3) Terms**\nA member of the Working Group shall be appointed for the life of the Working Group.\n**(4) Vacancies**\n**(A) Vacancy before expiration of term**\nA member appointed to the Working Group to fill a vacancy occurring before the expiration of the term for which the member\u2019s predecessor was appointed shall be appointed only for the remainder of that term.\n**(B) Manner of appointment**\nA vacancy in the Working Group shall be filled in the manner in which the original appointment was made.\n**(5) Compensation**\nA member of the Working Group shall serve without pay.\n**(6) Quorum**\nA majority of the members of the Working Group shall constitute a quorum, but a lesser number may hold hearings.\n**(7) Chairperson**\nThe Chairperson of the Working Group shall be appointed by the Attorney General from the membership of the Working Group.\n**(8) Meetings**\nThe Working Group shall hold virtual meetings monthly, and any subgroup of the Working Group shall hold additional meetings as necessary.\n##### (d) Staff of working group; experts and consultants\n**(1) Staff**\nThe Chairperson of the Working Group may appoint and fix the pay of additional personnel as the Chairperson considers appropriate.\n**(2) Experts and consultants**\nThe Chairperson of the Working Group may procure temporary and intermittent services under section 3109(b) of title 5, United States Code.\n**(3) Detailees**\nUpon request of the Chairperson of the Working Group, the head of any Federal department or agency may detail, on a reimbursable basis, any of the personnel of that department or agency to the Working Group to assist in carrying out the duties of the Working Group under this Act.\n##### (e) Powers of the working group\n**(1) Subpoena power**\n**(A) By Working group**\nThe Working may subpoena witnesses and records related to the purposes of this Act.\n**(B) Enforcement**\nThe district courts of the United States have jurisdiction to enforce a subpoena issued under this section. Trial is in the district in which the proceeding is conducted. The court may punish a refusal to obey a subpoena as a contempt of court.\n**(2) Hearings and Sessions**\n**(A) In general**\nThe Working Group may, for the purpose of carrying out this Act, hold hearings, sit and act at times and places, take testimony, and receive evidence as the Working Group considers appropriate.\n**(B) Witnesses**\nThe Working Group may administer oaths or affirmations to witnesses appearing before the Working Group.\n**(3) Powers of members and agents**\nAny member or agent of the Working Group may, if authorized by the Chairperson, take any action that the Working Group is authorized to take under this Section, including requesting information.\n**(4) Obtaining Official Information**\n**(A) United States Agencies and Departments**\n**(i) In general**\nThe Working Group may secure directly from any department or agency of the United States information necessary to enable the Working Group to carry out this Act.\n**(ii) Furnishing information**\nUpon request of the Chairperson of the Working Group for information solicited pursuant to subsection (b), the head of the department or agency of the United States shall furnish that information to the Working Group.\n**(B) State and Local Information**\n**(i) In general**\nThe Working Group may obtain and review information and data from State and local departments and agencies for purposes of carrying out this Act.\n**(ii) Costs**\nThe Working Group shall pay reasonable costs to state and local agencies for records obtained pursuant to subsection (b).\n**(5) Clearance for members of Working Group**\nIn the case that the Working Group interacts with controlled unclassified information, the Working Group shall follow all laws, regulations, and government-wide policies with respect to such information.\n##### (f) Termination of working group\n**(1) In general**\nThe Working Group shall terminate 120 days after submission of the report under section 9, unless the Attorney General determines that such termination is not appropriate.\n**(2) Reconvening group**\nIf the Working Group terminates under subsection (a), the Attorney General may reconvene the Working Group in accordance with this Act. If the Attorney General reconvenes the Working Group, the Working Group shall be convened in accordance with this section. The Attorney General may re-appoint members to the Working Group who served a previous term if the Working Group is reconvened.\n##### (g) Definitions\nIn this section:\n**(1) Child**\nThe term child means any individual under the age of eighteen years.\n**(2) Child sexual abuse material**\nThe term child sexual abuse material shall have the meaning given the term child pornography in section 2256 of title 18, United States Code.\n**(3) Crime involving sexual contact**\nThe term crime involving sexual contact means\u2014\n**(A)**\nan offense involving a child under chapter 109A of title 18, United States Code, or any attempt or conspiracy to commit such an offense; or\n**(B)**\nan offense involving a child under a State or Tribal statute that is similar to a provision described in subparagraph (A).\n**(4) Known to law enforcement**\nThe term known to law enforcement means that a Federal, State, Tribal, or local law enforcement agency has evidence of a crime that can be attributed to a person or location, including an email address, Internet Protocol address, screen name, universally unique identifier, phone number, or other information attributable to that person or location.\n**(5) Law enforcement agency**\nThe term law enforcement agency means an agency of the Federal Government, a State, a political subdivision of a State, or a federally recognized tribe that is authorized by law to supervise the prevention, detection, investigation, or prosecution of any violation of criminal law.\n**(6) NCMEC**\nThe term NCMEC means the National Center for Missing & Exploited Children.\n**(7) Proactive policing**\nThe term proactive policing means a covert or undercover investigation conducted by a law enforcement agency that involves a person or organization that the law enforcement agency believes is engaging or has engaged in an offense or violation relating to child sexual abuse, child sexual abuse material, child exploitation, or child sex trafficking crimes.\n**(8) State**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, or any other territory or possession of the United States.\n**(9) Victim-centric**\nThe term victim-centric refers to the systematic focus on the needs and concerns of a victim to ensure that services are delivered in a compassionate, sensitive, non-judgmental, and culturally considerate manner that seeks to minimize retraumatization associated with the criminal justice process by providing the support of victim advocates and service providers, empowering victims as engaged participants in the process, and providing victims an opportunity to play a role in seeing their abusers brought to justice.\n**(10) United States**\nThe term United States means the 50 States of the United States of America and the District of Columbia, the Commonwealth of Puerto Rico, Guam, the Virgin Islands, American Samoa, Wake Island, Midway Islands, Kingman Reef, Johnston Atoll, the Northern Mariana Islands, and any other trust territory or possession of the United States.",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-15T20:08:42Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5538ih.xml"
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
      "title": "Child Rescue Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-08T09:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Child Rescue Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-08T09:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Attorney General to convene a national working group to study proactive strategies and needed resources for the identification and rescue of children from sexual exploitation and abuse, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-08T09:03:14Z"
    }
  ]
}
```
