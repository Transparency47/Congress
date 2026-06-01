# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4500
- Title: VICTIM Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4500
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-28T14:45:32Z
- Update date including text: 2026-05-28T14:45:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in Senate
- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-12: Introduced in Senate

## Actions

- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4500",
    "number": "4500",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "VICTIM Act of 2026",
    "type": "S",
    "updateDate": "2026-05-28T14:45:32Z",
    "updateDateIncludingText": "2026-05-28T14:45:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T19:11:59Z",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4500is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4500\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Mr. Kennedy (for himself and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to establish a grant program to establish, implement, and administer violent incident clearance and technology investigative methods, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Violent Incident Clearance and Technological Investigative Methods Act of 2026 or the VICTIM Act of 2026 .\n#### 2. Grant program with respect to violent incident clearance and technological investigative methods\n##### (a) Definitions\nIn this section:\n**(1) Clearance by arrest**\nThe term clearance by arrest , with respect to an offense reported to a law enforcement agency, means the law enforcement agency\u2014\n**(A)**\nhas\u2014\n**(i)**\narrested not less than 1 person for the offense;\n**(ii)**\ncharged the person described in clause (i) with the commission of the offense; and\n**(iii)**\nreferred the person described in clause (i) for prosecution for the offense; or\n**(B)**\nhas cited an individual under the age of 18 to appear in juvenile court or before another juvenile authority with respect to the offense, regardless of whether a physical arrest occurred.\n**(2) Clearance by exception**\nThe term clearance by exception , with respect to an offense reported to a law enforcement agency, means the law enforcement agency\u2014\n**(A)**\nhas identified not less than 1 person suspected of the offense; and\n**(B)**\nwith respect to the suspect described in subparagraph (A), has\u2014\n**(i)**\ngathered enough evidence to\u2014\n**(I)**\nsupport an arrest of the suspect;\n**(II)**\nmake a charge against the suspect; and\n**(III)**\nrefer the suspect for prosecution;\n**(ii)**\nidentified the location of the suspect so that the suspect could be taken into custody immediately; and\n**(iii)**\nencountered a circumstance outside the control of the law enforcement agency that prohibits the agency from arresting the suspect, charging the suspect, or referring the suspect for prosecution, including\u2014\n**(I)**\nthe death of the suspect;\n**(II)**\nthe refusal of the victim to cooperate with the prosecution after the suspect has been identified; or\n**(III)**\nthe denial of extradition because the suspect committed an offense in another jurisdiction and is being prosecuted for that offense.\n**(3) Clearance rate**\nThe term clearance rate , with respect to a law enforcement agency, means the quotient obtained by dividing\u2014\n**(A)**\nthe number of offenses cleared by the law enforcement agency, including through clearance by arrest and clearance by exception; by\n**(B)**\nthe total number of offenses reported to the law enforcement agency.\n**(4) Eligible entity**\nThe term eligible entity means a State, Tribal, or local law enforcement agency or a group of such law enforcement agencies.\n**(5) Grant recipient**\nThe term grant recipient means a recipient of a grant under the Program.\n**(6) Law enforcement agency**\nThe term law enforcement agency means a public agency charged with policing functions, including any component bureau of the agency (such as a governmental victim services program or village public safety officer program), including an agency composed of officers or persons referred to in subparagraph (B) or (C) of section 2(10) of the Indian Law Enforcement Reform Act ( 25 U.S.C. 2801(10) ).\n**(7) Program**\nThe term Program means the grant program established under subsection (b)(1).\n**(8) Rural**\nThe term rural means an area that is not located in a metropolitan statistical area, as defined by the Office of Management and Budget.\n##### (b) Grant program\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall establish a grant program within the Office of Community Oriented Policing Services under which the Attorney General awards grants to eligible entities to establish, implement, and administer violent incident clearance and technological investigative methods.\n**(2) Applications**\nAn eligible entity seeking a grant under the Program shall submit to the Attorney General an application at such time, in such manner, and containing or accompanied by\u2014\n**(A)**\nsuch information as the Attorney General may reasonably require; and\n**(B)**\na description of each eligible project under paragraph (4) that the grant will fund.\n**(3) Selection of grant recipients**\nThe Attorney General, in selecting a recipient of a grant under the Program, shall\u2014\n**(A)**\nconsider solely the specific plan and activities proposed by the applicant to improve clearance rates for homicides and firearm-related violent crimes, notwithstanding other Department policies for grant eligibility; and\n**(B)**\ndevelop criteria to ensure that funds are distributed to rural and urban applicants.\n**(4) Eligible projects**\nA grant recipient shall use the grant for activities with the specific objective of improving clearance rates for homicides and firearm-related violent crimes, including\u2014\n**(A)**\nhiring and training additional personnel who will be assigned to investigate homicides and firearm-related violent crimes;\n**(B)**\nensuring the retention of personnel who are assigned to investigate homicides and firearm-related violent crimes as of the date of receipt of the grant;\n**(C)**\nhiring and training personnel for collection, processing, and forensic testing of evidence;\n**(D)**\nacquiring, upgrading, or replacing investigative, evidence-processing, or forensic testing technology or equipment;\n**(E)**\ndeveloping competitive and evidence-based programs to improve clearance rates for homicides and firearm-related violent crimes;\n**(F)**\nhiring and training of personnel to analyze violent crime and the temporal and geographic trends among homicides and firearm-related violent crimes;\n**(G)**\nretaining experts to conduct a detailed analysis of homicides and firearm-related violent crimes using Gun Violence Problem Analysis (commonly known as GVPA ) or a similar research methodology;\n**(H)**\ndevelopment and implementation of policies that safeguard civil rights and civil liberties during the collection, processing, and forensic testing of evidence;\n**(I)**\nestablishing programs to support officers who experience stress or trauma as a result of responding to or investigating homicides or other violent crime incidents;\n**(J)**\ndeveloping policies, procedures, and training to improve clearance rates for homicides and firearm-related violent crimes, including implementing best practices relating to\u2014\n**(i)**\nimproving internal agency cooperation, organizational oversight and accountability, and supervision of investigations;\n**(ii)**\ndeveloping specific goals and performance metrics for both investigators and investigative units;\n**(iii)**\nstrengthening relationships with communities the agency serves; and\n**(iv)**\ncollaboration with and among other law enforcement agencies and criminal justice organizations;\n**(K)**\nensuring victims of firearm-related violent crimes, and family members of victims of homicides, have appropriate access to emergency food, housing, clothing, travel, and transportation;\n**(L)**\ntraining to address the needs of victims of firearm-related violent crimes, and family members of victims of homicides, or collaborating with trained victim advocates and specialists to better meet the needs of victims and family members of victims;\n**(M)**\ndeveloping best practices for improving access to and acceptance of victim services, including victim services that promote medical and psychological wellness, ongoing counseling, legal advice, and financial compensation;\n**(N)**\ntraining personnel in trauma-informed interview techniques; and\n**(O)**\nensuring language and disability access supports are provided to victims and their families so that victims can exercise their rights and participate in the criminal justice process.\n##### (c) Supplement, not supplant\nGrant funds made available under this section shall be used to supplement, not supplant, Federal and non-Federal funds available for carrying out the activities described in this section.\n##### (d) Hiring\nA grant recipient using funds for hiring personnel under subsection (b)(4)(A) shall make a good faith effort to determine whether an applicant with prior law enforcement experience has a disciplinary record or internal investigation record by\u2014\n**(1)**\nconducting a search of the National Decertification Index and, if available, the National Law Enforcement Accountability Database; or\n**(2)**\nrequesting the personnel record of the applicant from each law enforcement agency that employed the applicant.\n##### (e) Report by grant recipient\nNot later than 1 year after receiving a grant under the Program, and each year thereafter until a final report is submitted regarding fiscal year 2032, a grant recipient shall submit to the Attorney General a report on the activities carried out using the grant during the preceding fiscal year, including, if applicable\u2014\n**(1)**\nthe number of personnel assigned to investigate homicides and firearm-related violent crimes hired by the grant recipient;\n**(2)**\nthe number of personnel hired for collecting, processing, and forensic testing of evidence by the grant recipient;\n**(3)**\na description of any training that is designed to assist in the solving of homicides and firearm-related violent crimes and improve clearance rates;\n**(4)**\nany new investigative, evidence-processing, or forensic technology or equipment purchased or any upgrades made to existing (as of the date on which the grant was awarded) investigative, evidence-processing, or forensic technology or equipment, and the associated cost;\n**(5)**\nan assessment of investigative, evidence-processing, or forensic technology or equipment purchased with the grant to determine whether the technology or equipment satisfies the objectives of the use of the technology or equipment in increasing clearance rates, and any policies in place to govern the use of the technology or equipment;\n**(6)**\nthe internal policies and oversight used to ensure that any technology purchased through the grant for the purposes of improving clearance rates does not violate the civil rights and civil liberties of individuals;\n**(7)**\ndata regarding clearance rates for homicides and firearm-related violent crimes, including the rate of clearances by arrest and clearances by exception, and crime trends from within each jurisdiction in which the grant recipient carried out activities supported by the grant;\n**(8)**\ndata on the race, sex, and age of victims of homicides and firearm-related violent crimes;\n**(9)**\ndata on the race, sex, and age of suspects of homicides and firearm-related violent crimes;\n**(10)**\nthe length and outcomes of each investigation, including whether the investigation was cleared by arrest or exception; and\n**(11)**\nto the extent reasonably available, identification of the services most used by victims and their families and identification of additional services needed.\n##### (f) Clearance Rate Reporting\nIf 2 or more law enforcement agencies collaborate on a criminal investigation that results in a clearance, only the agency that initiated the investigation shall include that clearance in the report submitted under subsection (e).\n##### (g) Grant oversight\n**(1) In general**\nAll grants awarded by the Attorney General under this section shall be subject to the requirements under this subsection.\n**(2) Audit requirement**\n**(A) Definition**\nIn this paragraph, the term unresolved audit finding means a finding in the final audit report of the Inspector General of the Department of Justice that the audited grant recipient has used grant funds for an unauthorized expenditure or otherwise unallowable cost that is not closed or resolved within 12 months from the date on which the final audit report is issued.\n**(B) Audits**\n**(i) In general**\nNot later than the first fiscal year after the date of establishment of the Program, and in each fiscal year thereafter, the Inspector General of the Department of Justice shall conduct audits of grant recipients under this section to prevent waste, fraud, and abuse of funds by grant recipients.\n**(ii) Selection of grant recipients for audit**\nThe Inspector General of the Department of Justice shall determine the appropriate number of grant recipients to be audited each year.\n**(C) Mandatory exclusion**\nA grant recipient that is found to have an unresolved audit finding shall not be eligible to receive grant funds under this section during the fiscal year following the 12-month period after the final audit report has been issued.\n**(3) Annual certification**\nNot later than the end of the fiscal year during which audits commence under paragraph (2)(B)(i), and each fiscal year thereafter, the Attorney General shall submit to the Committee on the Judiciary and the Committee on Appropriations of the Senate and the Committee on the Judiciary and the Committee on Appropriations of the House of Representatives a certification, including\u2014\n**(A)**\nwhether\u2014\n**(i)**\nall audits conducted by the Office of the Inspector General of the Department of Justice under paragraph (2) have been completed and reviewed by the appropriate Assistant Attorney General; and\n**(ii)**\nall mandatory exclusions required under paragraph (2)(C) have been issued; and\n**(B)**\na list of any grant recipients excluded from receiving grant funds under paragraph (2)(C) from the previous fiscal year.\n##### (h) National institute of justice evaluation and report to congress\n**(1) Evaluation**\nNot later than 2 years after the date of enactment of this Act, and every 2 years thereafter, the Director of the National Institute of Justice shall conduct an evaluation of\u2014\n**(A)**\nthe practices deployed by grant recipients to identify policies and procedures that have successfully improved clearance rates for homicides and firearm-related violent crimes; and\n**(B)**\nthe efficacy of any services provided to victims and family members of victims of homicides and firearm-related violent crimes.\n**(2) Report to Congress**\nNot later than 30 days after completion of an evaluation by the Director of the National Institute of Justice under paragraph (1), the Attorney General shall submit to Congress a report including\u2014\n**(A)**\nthe results of the evaluation; and\n**(B)**\ninformation reported by each grant recipient under subsection (e).\n##### (i) Application Process\n**(1) Barriers**\nThe Attorney General shall determine whether barriers exist to establishing a streamlined application process for grants under this section.\n**(2) Report**\n**(A) In general**\nNot later than 60 days after the date of enactment of this Act, the Attorney General shall submit to Congress a report that includes a plan to implement a streamlined application process for grants under this section under which an eligible entity seeking a grant under this section can reasonably complete the application in not more than 2 hours.\n**(B) Contents of plan**\nThe plan required under subparagraph (A) may include a plan for\u2014\n**(i)**\nproactively providing eligible local governments seeking a grant under this section with information on the data such eligible local governments will need to prepare before beginning the grant application; and\n**(ii)**\nensuring technical assistance is available for eligible local governments seeking a grant under this section before and during the grant application process, including through dedicated liaisons within the Office of Community Oriented Policing Services.\n**(3) Applications**\nIn selecting eligible local governments to receive grants under this section, the Director of the Office of Community Oriented Policing Services shall use the streamlined application process described in paragraph (2)(A).\n##### (j) Consultation\nThe Attorney General shall develop criteria governing the award of grants under this section to ensure that the funds are distributed as widely as practicable in terms of geographical location and to both large and small law enforcement agencies.\n##### (k) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to carry out this section $60,000,000 for each of fiscal years 2027 through 2031.\n**(2) Percent for certain eligible entities or projects**\n**(A) Tribal entities**\nThe Attorney General shall use at least 5 percent of the amount made available under paragraph (1) for a fiscal year to award grants under the Program to Tribal law enforcement agencies or Tribal prosecuting offices, or groups of such agencies or offices.\n**(B) Rural entities**\nThe Attorney General shall use at least 5 percent of the amount made available under paragraph (1) for a fiscal year to award grants under the Program to law enforcement agencies classified as rural.",
      "versionDate": "2026-05-12",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-28T14:45:32Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4500is.xml"
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
      "title": "VICTIM Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T03:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VICTIM Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Violent Incident Clearance and Technological Investigative Methods Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Attorney General to establish a grant program to establish, implement, and administer violent incident clearance and technology investigative methods, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T03:03:31Z"
    }
  ]
}
```
