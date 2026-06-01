# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2203?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2203
- Title: Break the Cycle of Violence Act
- Congress: 119
- Bill type: S
- Bill number: 2203
- Origin chamber: Senate
- Introduced date: 2025-06-28
- Update date: 2026-01-06T12:04:06Z
- Update date including text: 2026-01-06T12:04:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-28: Introduced in Senate
- 2025-06-28 - IntroReferral: Introduced in Senate
- 2025-06-28 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-28: Introduced in Senate

## Actions

- 2025-06-28 - IntroReferral: Introduced in Senate
- 2025-06-28 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-28",
    "latestAction": {
      "actionDate": "2025-06-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2203",
    "number": "2203",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Break the Cycle of Violence Act",
    "type": "S",
    "updateDate": "2026-01-06T12:04:06Z",
    "updateDateIncludingText": "2026-01-06T12:04:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-28",
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
      "actionDate": "2025-06-28",
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
        "item": [
          {
            "date": "2025-06-28T20:45:09Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-28T20:45:09Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "DE"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "CT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "DE"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-28",
      "state": "VT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "MA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "MN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "MA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "IL"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "WI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "OR"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "NY"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "HI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "RI"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "NY"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-28",
      "state": "RI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MN"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "IL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-01-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2203is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2203\nIN THE SENATE OF THE UNITED STATES\nJune 28, 2025 Mr. Booker (for himself, Ms. Blunt Rochester , Mr. Blumenthal , Mr. Coons , Mr. Murphy , Mr. Padilla , Mr. Sanders , Mr. Markey , Ms. Smith , Ms. Warren , Ms. Duckworth , Ms. Baldwin , Mr. Wyden , Mrs. Gillibrand , Ms. Hirono , Mr. Reed , Mr. Schumer , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize the Secretary of Health and Human Services to build safer, thriving communities, and save lives, by investing in effective community-based violence reduction initiatives, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Break the Cycle of Violence Act .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings.\nSec. 3. Definitions.\nTITLE I\u2014Department of Health and Human Services\nSec. 101. Community-based violence intervention program grants.\nSec. 102. Office of Community Violence Intervention.\nSec. 103. Community Violence Intervention Advisory Committee.\nSec. 104. Establishment of a National Community Violence Response Center.\nSec. 105. Sense of Congress regarding services for victims of violent crime.\nSec. 106. Authorization of appropriations.\nTITLE II\u2014Department of Labor\nSec. 201. Improving approaches for communities to thrive (IMPACT) grants.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCommunity violence is a significant public health, public safety, and community infrastructure concern nationwide, and is a leading cause of death, injury, and trauma for people in the United States. Community violence also disrupts employment and hinders a community\u2019s social and economic development. Today, gun violence is the leading cause of death for America\u2019s youth.\n**(2)**\nFrom 2010 to 2021, over 233,000 people were murdered in the United States. Hundreds of thousands more were hospitalized or treated in emergency departments after surviving life-changing gunshot injuries and other violent assaults.\n**(3)**\nIn 2020, the Nation suffered the largest single-year spike in homicides on record, driven largely by record spikes in fatal shootings. As of 2021, 80 percent of all homicides in the United States are committed with a gun.\n**(4)**\nCommunities across the Nation experience enormous disparities in safety that are driven by inequitable social and structural determinants of health. Interpersonal shootings are disproportionately concentrated in neighborhoods harmed by past and present racial discrimination, segregation, redlining, disinvestment, mass incarceration, and concentrated poverty, and this violence\u2019s toll falls overwhelmingly on people of color, especially young Black and Brown men and boys and their loved ones. From 2015 to 2020, Black children and teens were more than 12 times as likely to be shot to death as their White peers. Hispanic children and teens and Native American children and teens were both about 2.6 times as likely to be shot to death as their White peers. Over this period, 72 percent of children murdered before their 18th birthday were people of color, and more than 50 percent were Black.\n**(5)**\nBlack boys and men make up less than 7 percent of the population in the United States, but account for more than 50 percent of all gun homicide victims each year. Violence is responsible for nearly half of all deaths among Black boys and young men, ages 15 through 24, meaning the parents of a Black son in this age group are as likely to lose their child to homicide as nearly every other cause of death combined.\n**(6)**\nThis violence imposes enormous human, social, and economic consequences. Studies show that gun violence has a national economic cost of $557,000,000,000 annually. The Director of the Centers for Disease Control and Prevention\u2019s Division of Violence Prevention presented research to Congress demonstrating that youth living in inner cities show a higher prevalence of post-traumatic stress disorder than soldiers in the Nation\u2019s wartime military. While the vast majority of these young people resiliently persevere, people who have been victims of violence are at substantially higher risk of being violently reattacked or killed. Additionally, both direct and indirect violence exposure have been associated with a host of poor health outcomes, including chronic illness, anxiety, depression, and substance misuse.\n**(7)**\nWhen properly implemented and consistently funded, coordinated, community-based strategies that utilize trauma-responsive care and interrupt cycles of violence can produce lifesaving and cost-saving results in a short period of time without contributing to mass incarceration. These strategies identify those at the highest risk, coordinate individualized wraparound resources, provide pathways to healing and stability, and monitor and support long-term success. Many cities have substantially reduced community violence in recent years by implementing various combinations of these strategies, which include the following:\n**(A)**\nCommunity outreach programs, which hire violence intervention and prevention specialists who have established relationships, relatable lived experiences, and credibility with individuals in their communities at high risk of violence and connect them with intensive counseling, mediation, peer support, and social services in order to reduce their risk. Evaluations have found that these programs, particularly when integrated into wider networks of supportive services, are frequently associated with significant reductions in gun violence. A recent study of Safe Streets Baltimore looked at data from 2007 to 2022 and found that this strategy was associated with a statistically significant 23 percent reduction in nonfatal shootings.\n**(B)**\nHospital-based violence intervention programs (referred to in this section as HVIP ), which work to break cycles of violence by leveraging credible violence intervention and prevention specialists to provide intensive counseling, peer support, case management, mediation, and social services to patients recovering from gunshot wounds and other violent injuries. Research has shown that violently injured patients are at high risk of retaliating with violence themselves or being revictimized by violence in the near future. Evaluations of HVIPs have found that patients who received HVIP services were often less likely to be convicted of a violent crime and less likely to be subsequently reinjured by violence than patients who did not receive HVIP services.\n**(C)**\nGroup violence interventions provide tailored social services and support to group-involved individuals at highest risk for involvement in community violence. This intervention, which must be trauma-informed, culturally responsive, and community-driven to be most successful, includes a process for community members to voice a clear demand for the violence to stop and narrowly focused enforcement actions against those who continue to engage in acts of serious violence. The approach coordinates law enforcement, service providers, and community engagement efforts to reduce violence in ways that do not contribute to mass incarceration.\n**(D)**\nViolence interruption and crisis management, which respond to potentially violent incidents to mediate conflicts or to scenes where violence has occurred to offer trauma-informed services and community supports to survivors and others exposed to violence. These strategies help to prevent retaliatory violence and promote healing and well-being. Programs that include these components have reported deescalating dozens of disputes that were highly likely to end in lethal violence.\n**(8)**\nAccess to job and entrepreneurship training, apprenticeship, and technological and digital literacy programs are effective tools in reducing community violence. A 2012 University of Pennsylvania study of 13 high-violence schools in the Chicago area found well-targeted, low-cost employment policies can make a substantial difference , and the city\u2019s most violent neighborhoods saw a 43 percent drop in violent-crime arrests of participants in a youth job program.\n**(9)**\nIndividualized wraparound services and opportunities include housing support, financial assistance, reentry services, legal assistance, therapeutic services, grief counseling or targeted victim services, and skill building based on the needs of survivors or individuals at the highest risk of community violence. Leveraging the relationships of violence intervention and prevention specialists, these services are used in the context of structured, person-centered peer mentorship that facilitates personal transformation by meeting people where they are and offering to help participants change the trajectories of their lives.\n**(10)**\nThe past year has had a disproportionate impact on youth unemployment, with 2,900,000 more unemployed youth in mid-2020 compared with pre-2020 levels. Simultaneously, the 2020 recession accelerated an already increasingly digital and automated workforce, and youth must attain the digital, technological, and other technical skills necessary to thrive in the future of work. While jobs in the customer service and food industry could fall by 4,300,000 between 2018 and 2030, health care and science, technology, engineering, and math occupations could grow more now than ever.\n**(11)**\nIntentional and sustained investments in community-based violence reduction strategies can reverse recent increases in homicides, help to heal impacted communities, and reduce the enormous human and economic costs of community violence, without contributing to mass incarceration.\n#### 3. Definitions\nIn this Act:\n**(1) Community violence**\nThe term community violence \u2014\n**(A)**\nmeans nonfatal firearm injuries, aggravated assaults, homicides, and other acts of life-threatening interpersonal violence committed outside the context of a familial or romantic relationship; and\n**(B)**\ndoes not include acts of violence motivated by political beliefs.\n**(2) Eligible unit of local government**\nThe term eligible unit of local government means a municipality or other local government that\u2014\n**(A)**\nfor not less than 2 out of the 3 calendar years preceding the date on which an application for a grant is submitted under section 101\u2014\n**(i)**\nexperienced 35 or more homicides per year; or\n**(ii)**\nexperienced 20 or more homicides per year and had a homicide rate that was not less than double the national average; or\n**(B)**\nhas a compelling need to address community violence, as determined by the Secretary, based on high levels of homicide relative to other localities within the same State.\n**(3) Opportunity youth**\nThe term opportunity youth means individuals who\u2014\n**(A)**\nhave attained 16 years of age but not yet attained 25 years of age; and\n**(B)**\nare not\u2014\n**(i)**\nenrolled in education or training on a full-time or part-time basis; or\n**(ii)**\nemployed on a full-time or part-time basis.\nI\nDepartment of Health and Human Services\n#### 101. Community-based violence intervention program grants\n##### (a) In general\nThe Secretary of Health and Human Services (in this title referred to as the Secretary ) shall award grants to eligible entities to support, enhance, and replicate coordinated community violence intervention.\n##### (b) Eligibility\nTo be eligible to seek a grant under this section, an entity shall be\u2014\n**(1)**\na community-based, nonprofit organization that\u2014\n**(A)**\nserves the residents served by an eligible unit of local government; and\n**(B)**\nhas a track record of providing community-related activities or support program innovation in communities of color; or\n**(2)**\nan eligible unit of local government.\n##### (c) Limitation\nOf the amount made available to carry out this title for a fiscal year, not more than 15 percent of such amount shall be made available to eligible units of local government.\n##### (d) Use of funds\n**(1) In general**\nA grant awarded under this section shall be used to implement coordinated community violence intervention initiatives, through coordinated, community-based strategies.\n**(2) Requirements**\nA community violence intervention initiative implemented using grant funds awarded under this section shall\u2014\n**(A)**\nbe primarily focused on providing culturally competent, community-based violence intervention services to the portion of a grantee\u2019s community who are, regardless of age, identified as being at high risk of being victimized by, or engaging in, community violence; and\n**(B)**\nuse strategies that\u2014\n**(i)**\nare evidence-informed and have demonstrated promise at reducing community violence without contributing to mass incarceration;\n**(ii)**\nutilize trauma-responsive care and interrupt cycles of violence;\n**(iii)**\nexpand economic opportunity through new jobs, educational opportunities, or training programs; and\n**(iv)**\nare primarily focused on individuals at high risk of being victimized by, or engaging in, community violence.\n**(3) Community partnerships**\n**(A) Eligible units of local government**\nEach eligible unit of local government awarded a grant under this section shall distribute not less than 75 percent of such grant funds to one or more of the following:\n**(i)**\nA community-based organization or nonprofit organization.\n**(ii)**\nA public agency or department that is primarily dedicated to the prevention of violence or to community safety, but is not a law enforcement agency.\n**(B) Hospitals**\nEach hospital awarded a grant under this section in the hospital\u2019s capacity as a community-based, nonprofit organization described in subsection (b)(1) shall distribute not less than 90 percent of such grant funds to one or more of the following:\n**(i)**\nA community-based organization or nonprofit organization that provides direct services to individuals who have been victimized by community violence.\n**(ii)**\nDirect program staff.\n**(iii)**\nIndividual subcontractors who provide direct program-related services.\n##### (e) Application requirements\nEach applicant for a grant under this section shall submit a grant proposal, which shall, at a minimum\u2014\n**(1)**\ndescribe how the applicant proposes to use the grant to implement a coordinated community violence intervention initiative in accordance with this section;\n**(2)**\ndescribe how the applicant proposes to use the grant to promote or improve coordination between relevant agencies and community organizations in order to minimize duplication of services, complement other community violence intervention efforts, and achieve maximum impact;\n**(3)**\nprovide evidence indicating that the proposed community violence intervention initiative would likely reduce community violence or address the trauma and collateral consequences for individuals at high risk of being victimized by, or engaging in, community violence;\n**(4)**\ndescribe how the applicant plans to ensure the community violence intervention initiative is implemented in a manner that is\u2014\n**(A)**\nevidence-informed; and\n**(B)**\ncoordinated with the programs and activities of other entities for addressing community violence; and\n**(5)**\nin the case of a unit of local government applicant, demonstrate strong support from community partners with experience engaging individuals at high risk of being victimized by, or engaging in, community violence, as demonstrated by\u2014\n**(A)**\nthe development of a community steering committee that\u2014\n**(i)**\nprovides advice and assistance to the locality in administering grants awarded under this section; and\n**(ii)**\nis composed of individuals who substantially reflect local populations impacted by community violence, including survivors of community violence and individuals with expertise in culturally competent and trauma-informed approaches to reducing community violence; and\n**(B)**\nletters of support from individuals, such as\u2014\n**(i)**\nthe mayor or chief executive officer of the unit of local government; and\n**(ii)**\nthe director of one or more community-based organizations that provide services to individuals at high risk of being victimized by, or engaging in, community violence.\n##### (f) Prioritization\nIn awarding grants under this section, the Secretary shall give preference to applicants whose grant proposals demonstrate the greatest likelihood of reducing community violence in the target area without contributing to mass incarceration.\n##### (g) Grant duration\nA grant awarded under this section shall be for a 4-year period.\n##### (h) Grant award\nThe amount awarded to an applicant under this section shall be commensurate with\u2014\n**(1)**\nthe scope of the proposal; and\n**(2)**\nthe demonstrated need for additional resources to effectively reduce community violence in the applicant\u2019s community.\n##### (i) Matching funds required\n**(1) In general**\nExcept as provided in paragraphs (2) and (3), the Federal share of each grant awarded under this section shall be 90 percent of the eligible costs incurred by the grant recipient.\n**(2) Exemption from requirement**\nParagraph (1) shall not apply to a grant awarded to a community-based organization described in subsection (b)(1).\n**(3) Waiver**\nThe Federal share of a grant awarded to a unit of local government (that is an eligible entity under subsection (b)(2)) may be up to 100 percent if the Secretary determines there is good cause to waive the Federal share requirement under paragraph (1) of this subsection.\n##### (j) Reports\nNot later than 1 year after the date on which the first 4-year grant period under this section ends, the Secretary shall publish a report identifying best practices for grantees under this section to implement community-based violence intervention initiatives.\n##### (k) Rewarding success\n**(1) In general**\nThe Secretary may reserve not more than 10 percent of the funds appropriated for a fiscal year to carry out this title for supplemental incentive funds to be distributed to grantees outside the competitive grant process in accordance with paragraph (2).\n**(2) Distribution of additional funds**\nThe Secretary may distribute amounts reserved under paragraph (1), in the discretion of the Secretary, to grantees under subsection (a) that have\u2014\n**(A)**\nimplemented the grant for not less than 2 years;\n**(B)**\ndemonstrated exceptional commitment and progress toward implementing the grantee\u2019s community violence reduction initiative; and\n**(C)**\nshown that the grantee would likely achieve more substantial reductions in community violence with additional Federal funding.\n**(3) Federal share**\nSubsection (i) shall not apply to any amounts distributed to a grantee under this subsection.\n**(4) Explanation of distribution**\nUpon distributing supplemental incentive funds to a grantee, the Secretary shall publish a statement on the website of the Department of Health and Human Services that clearly explains the basis for the decision to award such funds to a particular grantee.\n##### (l) Evaluation and intensive site implementation support\nThe Secretary may reserve not more than 8 percent of the funds appropriated for a fiscal year to carry out this title for the purpose of\u2014\n**(1)**\ncontracting with or hiring intensive site implementation providers with experience implementing community violence intervention strategies;\n**(2)**\nproviding grants to applicants under subsection (a) that provide training and certification to community violence intervention and prevention professionals in order to expand the field and build capacity of frontline workers and other providers; and\n**(3)**\ncontracting with independent researchers to evaluate the implementation, performance, and impact of selected initiatives supported by the grants made under this section, which evaluations shall be made publicly available on the website of the Department of Health and Human Services.\n##### (m) Supplement, not supplant\nA grantee receiving a grant under this section shall use the grant to supplement, and not supplant, the amount of funds the grantee would otherwise dedicate to a community violence intervention initiative.\n#### 102. Office of Community Violence Intervention\n##### (a) Establishment\nThe Secretary shall establish within the Department of Health and Human Services, the Office of Community Violence Intervention (in this title referred to as the Office ), to be headed by a director.\n##### (b) Duties\nThe Secretary shall delegate to the Director of the Office responsibility for implementing the provisions of this title.\n##### (c) Reservation\nOf the amount made available to carry out this title for a fiscal year, the Secretary shall reserve not more than 5 percent for the administrative expenses of the Office.\n#### 103. Community Violence Intervention Advisory Committee\n##### (a) Establishment\nThe Secretary shall establish a Community Violence Intervention Advisory Committee (in this title referred to as the Advisory Committee ) to provide advice and assistance to the Secretary and Office in carrying out this title, including\u2014\n**(1)**\ndevelopment of grant solicitations;\n**(2)**\nraising awareness about grant solicitations among potentially eligible units of government and organizations;\n**(3)**\nselection of grant proposals;\n**(4)**\nselection of grantees to receive supplemental funds in accordance with section 101(k); and\n**(5)**\nformation of the National Community Violence Response Center under section 104.\n##### (b) Members\nIn appointing members of the Advisory Committee, the Secretary shall\u2014\n**(1)**\nappoint the members from among individuals with expertise implementing or evaluating community violence intervention initiatives;\n**(2)**\ninclude a representative with expertise in workforce development selected by the Secretary of Labor;\n**(3)**\nensure the membership of the Advisory Committee reflects a commitment to culturally competent and trauma-informed approaches to preventing violence among individuals at high risk of violence; and\n**(4)**\nensure that the members of the Advisory Committee include substantial representation of communities of color disproportionately impacted by community violence.\n#### 104. Establishment of a National Community Violence Response Center\n##### (a) Establishment\nThe Secretary shall establish and operate a National Community Violence Response Center (referred to in this section as the Center ).\n##### (b) Duties\nThe Center shall have the following roles and responsibilities:\n**(1) Assessment; technical assistance**\nThe Office and the Center, with the advice of the Advisory Committee, shall\u2014\n**(A)**\ndevelop a 4-tier taxonomy to assess the maturity of community violence infrastructure among grantees under section 101; and\n**(B)**\nprovide technical assistance to grantees under section 101 in the implementation of coordinated community violence intervention funded through the grant.\n**(2) Intensive site implementation support**\nThe Center shall\u2014\n**(A)**\ndevelop intensive site implementation support for each of the 4 tiers to maximize the effectiveness of the development of community violence initiatives;\n**(B)**\ndevelop intensive site implementation support for each eligible unit of local government that is a grant recipient to assess the contours of the community violence within the jurisdiction and identify relevant community-based interventions that may be successful at preventing future community violence; and\n**(C)**\nprovide ongoing support to community-based organizations to facilitate site infrastructure building, program implementation and operation, and quality improvement assistance.\n**(3) Data Collection**\n**(A) Policies**\nThe Office and the Center shall develop data collection policies for grant recipients that measure safety, community health, opportunity youth engagement, economic development, and recidivism.\n**(B) Assistance**\nThe Center shall assist grant recipients in establishing data collection systems and practices, and collect data from the grant recipients.\n**(4) Research coordination**\n**(A) Establishment of advisory council**\nThe Center, in consultation with nonprofit, nongovernmental organizations and researchers whose primary expertise is in community violence, shall establish a Community Violence Research Advisory Council (in this paragraph referred to as the Research Advisory Council )\u2014\n**(i)**\nto coordinate research on community violence; and\n**(ii)**\nto report to Congress on any gaps on issues related to community violence.\n**(B) Membership**\nThe Research Advisory Council shall include representatives from\u2014\n**(i)**\nall Federal agencies that fund research on community violence; and\n**(ii)**\nthe Bureau of Labor Statistics.\n**(C) Duties**\nThe Research Advisory Council shall provide advice and assistance to the Center to\u2014\n**(i)**\ndevelop a coordinated strategy to strengthen research focused on community violence education, prevention, and intervention strategies;\n**(ii)**\ntrack and report all Federal research and expenditures related to community violence; and\n**(iii)**\nidentify gaps in community violence research, governmental expenditures on community violence issues, and promising strategies that have not yet been rigorously evaluated.\n**(5) Conferral**\n**(A) In general**\nThe Center shall establish a biennial conference to include\u2014\n**(i)**\ngrantees and providers of intensive site implementation support in the community violence field that receive funding under this title or title II; and\n**(ii)**\nother key stakeholders.\n**(B) Topics**\nThe topics to be addressed at the biennial conference shall include\u2014\n**(i)**\nthe administration of grants;\n**(ii)**\nchallenges and gaps in community violence intervention initiatives;\n**(iii)**\nstrategies for overcoming such challenges and gaps;\n**(iv)**\npromising practices in the field; and\n**(v)**\nemerging trends.\n**(C) Report**\nNot later than 90 days after the conclusion of each biennial conference, the Center shall publish a comprehensive report that\u2014\n**(i)**\nsummarizes the issues presented during the conference and what, if any, policies the Center intends to implement to address those issues; and\n**(ii)**\nis made available to the public on the Center\u2019s website and submitted to Congress.\n**(6) Capacity building and fostering innovation**\nThe Center shall\u2014\n**(A)**\npromote expansion and development of the field of community violence intervention and prevention, including fostering collaboration, information-sharing, and dissemination of best practices among practitioners, providers of intensive site implementation support, and programs and individuals working in the same regions or States, including the identification and dissemination to the public of best practices for addressing community violence;\n**(B)**\ndevelop a plan for expanding providers of intensive site implementation support in the field of community violence intervention and prevention;\n**(C)**\ndevelop a plan for identifying innovative community violence intervention and prevention strategies that are in need of further research and evaluation; and\n**(D)**\ndevelop a plan for providing ongoing intensive site support to organizations implementing community violence intervention and prevention strategies.\n**(7) Reporting**\nThe Center shall annually provide a report to Congress addressing topics to include\u2014\n**(A)**\nnational trends in community violence statistics;\n**(B)**\na summary of the activities of the Center and the Office under this title; and\n**(C)**\nrecommendations for improving the national response to community violence.\n#### 105. Sense of Congress regarding services for victims of violent crime\nIt is the sense of Congress that\u2014\n**(1)**\ncommunity-based violence intervention programs have shown effective results as a strategy in reducing the risk of reinjury of, or retaliation by, victims of community violence, and promoting victims\u2019 recovery and well-being;\n**(2)**\nyoung men, boys, girls, and women of color are disproportionately victimized by community violence, but are frequently underserved by victim service providers; and\n**(3)**\nStates and territories should consider using funding provided through the Crime Victims Fund to support community-based violence intervention initiatives that provide services for direct and secondary victims of community violence at high risk for reinjury and involvement in community violence.\n#### 106. Authorization of appropriations\nThere is authorized to be appropriated to the Department of Health and Human Services to carry out this title, in addition to any amounts otherwise authorized to be appropriated or made available to the Department of Health and Human Services for such purpose\u2014\n**(1)**\n$300,000,000 for fiscal year 2026;\n**(2)**\n$500,000,000 for fiscal year 2027; and\n**(3)**\n$700,000,000 for each of fiscal years 2028 through 2033.\nII\nDepartment of Labor\n#### 201. Improving approaches for communities to thrive (IMPACT) grants\n##### (a) In general\nThe Secretary of Labor (in this section referred to as the Secretary ) shall award grants to eligible entities for year-round job training and workforce programs authorized under section 129(c)(1) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3164(c) ), with the elements described in section 129(c)(2)(C) of such Act ( 29 U.S.C. 3164(c)(2)(C) ), for opportunity youth in communities disproportionately affected by gun violence for the purposes of connecting opportunity youth to in-demand occupations.\n##### (b) Eligibility\nTo be eligible to seek a grant under subsection (a), an entity shall be\u2014\n**(1)**\na community-based, nonprofit organization that\u2014\n**(A)**\nserves the residents served by an eligible unit of local government;\n**(B)**\nhas a track record of providing community-related activities or support program innovation in communities of color;\n**(C)**\nfocuses on training technical skills to prepare opportunity youth for in-demand occupations; and\n**(D)**\nprovides\u2014\n**(i)**\ntraining for opportunity youth who are basic skills deficient; and\n**(ii)**\nsoft skills training that enables opportunity youth to engage successfully in work culture;\n**(2)**\nan Indian Tribe or an agency primarily serving Native Americans;\n**(3)**\nan entity that carries out activities authorized under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ) that has a focus on opportunity youth;\n**(4)**\na federally or State recognized apprenticeship program;\n**(5)**\nan accredited community college; or\n**(6)**\nan eligible unit of local government.\n##### (c) Reporting\nThe Secretary shall require grantees under this section to report to the Secretary on primary measures funded under this section for\u2014\n**(1)**\nentry into job training, education, apprenticeship, skilled trades training, or other paid and unpaid work experiences that have as a component academic and occupational education programs; and\n**(2)**\nchanges in overall school enrollment, unemployment, or weekly earnings for opportunity youth participating in activities of the respective grantee.\n##### (d) Definitions\nIn this section:\n**(1) Basic skills deficient**\nThe term basic skills deficient means an individual who\u2014\n**(A)**\nis a youth and has English reading, writing, or computing skills at or below the 8th grade level on a generally accepted standardized test; or\n**(B)**\nis unable to compute or solve problems, or read, write, or speak English, at a level necessary to function on the job, in the individual\u2019s family, or in society.\n**(2) In-demand occupation**\nThe term in-demand occupation means an occupation described in section 3(23)(A)(ii) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102(23)(A)(ii) ).\n##### (e) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $1,500,000,000 for the period of fiscal years 2026 through 2033, to remain available until expended through fiscal year 2033.",
      "versionDate": "2025-06-28",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-06-24",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4103",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Break the Cycle of Violence Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-29T15:04:25Z"
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
      "date": "2025-06-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2203is.xml"
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
      "title": "Break the Cycle of Violence Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T12:04:06Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Break the Cycle of Violence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-17T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of Health and Human Services to build safer, thriving communities, and save lives, by investing in effective community-based violence reduction initiatives, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T02:18:16Z"
    }
  ]
}
```
